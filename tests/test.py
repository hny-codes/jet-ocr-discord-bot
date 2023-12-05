try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import requests
import io

response = requests.get(
    "https://cdn.discordapp.com/attachments/622593706998104107/1181382688964362301/Screenshot_2023-11-29_194102.png?ex=6580db5e&is=656e665e&hm=5781cfd69977b9755f946992ef38b61f6d6ed9d1c8dc80a5d642679c22087b7a&"
)
print("Response: ", response)

image = Image.open(io.BytesIO(response.content))
# image = Image.open('screenshot2.png')
print("Image: ", image)

tessdata_dir_config = r'--tessdata-dir "/home/tachi/Desktop/langs/tessdata"'

# text = pytesseract.image_to_string(
#     image=image, timeout=120, config=tessdata_dir_config, lang="eng+jpn"
# )

# Get language about picture
info = pytesseract.image_to_osd(image=image)
language = info.split("\n")[-3].split()[1]

print(language)

# Return OCR text based on language
text = (
    pytesseract.image_to_string(image=image, config=tessdata_dir_config, lang="jpn")
    if language == "Japanese"
    else pytesseract.image_to_string(image=image, config=tessdata_dir_config)
)

print(text)
