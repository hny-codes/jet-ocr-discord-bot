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
        print("Initiated Tesseract Reader")
        # Set psm to single column of text 
        self.psm = 4

    def get_language(self, image):
        """Get OSD detected language of image"""
        print("Getting language..")

        # Reduce minimum characters of target image to determine language
        # REFERENCE: https://stackoverflow.com/a/68978474
        config = r"--psm 0 -c min_characters_to_try=5"
        try:
            info = pytesseract.image_to_osd(image=image, config=config)
            print("Info: ", info)
            return info.split("\n")[-3].split()[1]
        except Exception as e:
            print("Error: ", e)

            # Set PSM to bypass tesseract segmentation, catch all
            self.psm = 3
            return "CatchAll"

    def parse_image(self, image):
        try:
            text = ""

            print("Parsing via pytesseract")

            # Get language of image
            language = self.get_language(image)
            print("Language: ", language, "\n")

            tessdata_dir_config = (
                f'--tessdata-dir "/home/tachi/Desktop/langs/tessdata" --psm {self.psm}'
            )

            if language == "Japanese" or language == "Katakana":
                text = pytesseract.image_to_string(
                    image=image, timeout=120, config=tessdata_dir_config, lang="jpn"
                )
            elif language == "Latin" or language == "Cyrillic":
                text = pytesseract.image_to_string(
                    image=image, config=tessdata_dir_config
                )
            else:
                catch_config = f'--tessdata-dir "/home/tachi/Desktop/langs/tessdata" -l jpn+eng --psm {self.psm}'
                text = pytesseract.image_to_string(
                    image=image, config=tessdata_dir_config
                )

            return text

        except RuntimeError as e:
            print(e)
