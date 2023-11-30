import requests
import io
from ocr_reader import ImageReader
try:
  from PIL import Image
except ImportError:
  import Image


def get_image(url):
  """ Parses an image URL and returns an PIL image """
  response = requests.get(url)
  image = Image.open(io.BytesIO(response.content))

  return image

def parse_image(img, lang):
  """ Grabs the text of a given image and returns it """
  response = requests.get(img)

  # Get image content and accuracy
  # lang = english default
  reader = ImageReader(response.content, lang)
  text = reader.get_text()
  return text