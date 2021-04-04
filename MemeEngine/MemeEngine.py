from random import randint
from PIL import Image, ImageDraw, ImageFont


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
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                                      size=20, encoding="unic")
        #font = ImageFont.load_default()


        max_x = (img.size[0]/2)
        min_x = (img.size[0]/10)

        range_x = randint(min_x, max_x)

        lines = [text, "- " + author] #make to unicode?

        line_height = font.getsize('hg')[1]

        # Calculate y axis

        min_y = (img.size[1]/20)

        max_y = img.size[1]

        max_y -= ((len(lines) + 1) * line_height)

        range_y = randint(int(min_y), int(max_y))

        for line in lines:

            draw.text((range_x, range_y), line, font=font, align="left")

            range_y += line_height

        op = f'{self.output_dir}/{randint(0,100000000)}.jpeg'

        img.save(op)

        return op
