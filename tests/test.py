try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import requests
import io

response = requests.get(
    "https://cdn.discordapp.com/attachments/939674781823959091/1180663574616616960/screenshot2.png?ex=657e3da3&is=656bc8a3&hm=484e6115ad18581cde0f365682646556aa5c2794cb829e2833bc76df0bbf66bc&"
)
print("Response: ", response)

image = Image.open(io.BytesIO(response.content))
# image = Image.open('screenshot2.png')
print("Image: ", image)

tessdata_dir_config = r'--tessdata-dir "/home/tachi/Desktop/langs/tessdata"'

text = pytesseract.image_to_string(
    image=image, timeout=120, config=tessdata_dir_config, lang="jpn"
)

print(text)
