import requests
import io

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2


class TesseractReader:
    def __init__(self):
        print('Initiated Tesseract Reader')

    def parse_image(self, image):
        try:
            tessdata_dir_config = r'--tessdata-dir "/home/tachi/Desktop/langs/tessdata"'
            print("Parsing via pytesseract")

            return pytesseract.image_to_string(
                image=image, timeout=120, config=tessdata_dir_config, lang='eng+jpn'
            )

        except RuntimeError as e:
            print(e)
