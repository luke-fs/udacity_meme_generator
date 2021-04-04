from random import randint
from PIL import Image, ImageDraw, ImageFont
import textwrap


class MemeEngine():

    def __init__(self, output_dir):
        """The init Method of the MemeEngine

        Args:
            output_dir: Output directory
        """
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a Meme with the quote and the Author details
        Arguments: img_path {str}: the file location for the image.
            text {str}: the quote that shoud be on image.
            width {int}: The pixel width value. Default=500.
            author {str}: author of quote.

        Returns: str:the file path to the output image.
        """

        img = Image.open(img_path)

        if width is not None:
            ratio = width/float(img.size[0])

            height = int(ratio*float(img.size[1]))

            img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)

        # doesnt worked on my OS
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20) #, encoding="unic"
        #font = ImageFont.load_default()


        max_x = (img.size[0]/2)
        min_x = (img.size[0]/10)

        range_x = randint(min_x, max_x)

        # .encode(encoding='UTF-8',errors='strict')
        ttext = text + "- " + author

        wrapper = textwrap.TextWrapper(width=50)
        word_lst = wrapper.wrap(text=ttext)
        text_new = ''
        for word in word_lst[:-1]:
            text_new = text_new + word + '\n'
        text_new += word_lst[-1]

        x, y = 100, 200
        draw.text((x, y), text_new, font=font,
                  align='center', stroke_width=1, stroke_fill='black')

        op = f'{self.output_dir}/{randint(0,100000000)}.jpeg'

        img.save(op)

        return op
