from PIL import Image, ImageDraw, ImageFont
from random import randint

class MemeEngine():

    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str: #generated image path

        """Create a Meme with quota and Author details
        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the quotation on image.
            author {str} -- The author of quote.
            width {int} -- The pixel width value. Default=500.
        
        Returns:
            str -- the file path to the output image.
        """

        print(img_path)
        img = Image.open(img_path)
        
        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width,height), Image.NEAREST)
        
        draw = ImageDraw.Draw(img)
        
        #font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
        #                              size=20)

        font = ImageFont.load_default()
        
        x_min = (img.size[0]/10)
        x_max = (img.size[0]/2)
        range_x = randint(x_min, x_max)

        lines = [text, "- " + author]
        line_height = font.getsize('hg')[1]   #Line Spacing

        # Calculate y axis for text display
        y_min = (img.size[1]/20)
        y_max = img.size[1]
        # avoid text overflow below + leave some space
        y_max -= ((len(lines) + 1) * line_height)
        range_y = randint(y_min, y_max)

        for line in lines:
            draw.text((range_x, range_y), line, font=font, align="left")
            range_y += line_height
        
        out_path = f'{self.output_dir}/{randint(0,100000000)}.jpeg'
        img.save(out_path)
        return out_path