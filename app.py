import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./src/_data/DogQuotes/DogQuotesTXT.txt',
                   './src/_data/DogQuotes/DogQuotesDOCX.docx',
                   './src/_data/DogQuotes/DogQuotesPDF.pdf',
                   './src/_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []

    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./src/_data/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # :
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # :
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    img = requests.get(image_url, allow_redirects=True)
    img_file = f'./static/{random.randint(0, 100000000)}.jpg'
    open(img_file, 'wb').write(img.content)
    path = meme.make_meme(img_file, body, author)

    os.remove(img_file)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
