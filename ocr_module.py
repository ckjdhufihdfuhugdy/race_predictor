"""OCR utilities for images and PDFs."""

from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from typing import Union


def ocr_image(image_file: Union[str, bytes]) -> str:
    """Extract text from an image file-like object or path."""
    image = Image.open(image_file)
    return pytesseract.image_to_string(image)


def ocr_pdf(pdf_file: Union[str, bytes]) -> str:
    """Extract text from each page of a PDF."""
    images = convert_from_path(pdf_file)
    return "\n".join(pytesseract.image_to_string(img) for img in images)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python ocr_module.py <image_or_pdf>")
        sys.exit(1)

    path = sys.argv[1]
    if path.lower().endswith(".pdf"):
        print(ocr_pdf(path))
    else:
        print(ocr_image(path))
