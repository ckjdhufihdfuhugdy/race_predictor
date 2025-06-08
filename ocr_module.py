# ocr_module.py
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import io

def ocr_image(image_file):
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    return text

def ocr_pdf(pdf_file):
    # Convert PDF to images
    images = convert_from_path(pdf_file)
    text = ''
    for img in images:
        text += pytesseract.image_to_string(img)
        text += '\n'
    return text
 # In Spyder, run this block (after running your ocr_module code):

from ocr_module import ocr_image

text = ocr_image("PATH/TO/YOUR/IMAGE.png")
print(text)   # Print output and copy-paste into chat here

# Now experiment with parsing:
from parse_module import parse_racecard_text

df = parse_racecard_text(text)
print(df)     # Or just view in Variable Explorer!
