import pytesseract
from urllib import request
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"

image = Image.open(r"captcha.png")
gray = image.convert('L')
gray.save('captcha_gray.png')
bw = gray.point(lambda x:0 if x<1 else 255,'1')
bw.save('captcha_thresholded.png')
text = pytesseract.image_to_string(bw)
print(text)
