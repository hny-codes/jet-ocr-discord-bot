import easyocr

class ImageReader():
  def __init__(self, image, lang='en'):
    self.image = image
    self.reader = easyocr.Reader([lang])

  def get_text(self):
    """ Grabs text off the image and returns the text and accuracy of the model """
    result = self.reader.readtext(self.image, detail=1)
    output = ''
    accuracy = 0

    for i in range(len(result)):
      output += result[i][1:][0] + '\n'
      accuracy += result[i][1:][1]

    # Find the average accuracy
    accuracy = round(accuracy / len(result), 2) * 100

    # Concat accuracy to end of results
    output += f'\n\n __Accuracy:__ **{accuracy}**%'

    return output