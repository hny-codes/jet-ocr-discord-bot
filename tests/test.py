import easyocr

reader = easyocr.Reader(['ch_sim', 'en'])
result = reader.readtext('tests\screenshot1.png', detail=0)

print(result)