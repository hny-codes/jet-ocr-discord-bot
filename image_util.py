import requests
import io
from ocr_reader import ImageReader
from tesseract_reader import TesseractReader

try:
    from PIL import Image
except ImportError:
    import Image


def get_image(url):
    """Parses an image URL and returns an PIL image"""
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content))

    return image


def parse_image(img):
    """Grabs the text of a given image and returns it"""
    response = requests.get(img)
    image = Image.open(io.BytesIO(response.content))
    print("Image: ", image)

    # Creates a TesseractReader object and send image to be parsed
    reader = TesseractReader()
    text = f"```{reader.parse_image(image)}```"
     
    return text if text != f"``````" else '```No text available```'
