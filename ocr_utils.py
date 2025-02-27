# utils/ocr_utils.py

import cv2                  # OpenCV for image processing
import numpy as np          # NumPy for numerical operations
import pytesseract          # Tesseract OCR for text extraction
from pdf2image import convert_from_bytes  # Converts PDF to images

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def preprocess_image(image):
    
    """
    Preprocess an image before OCR to improve accuracy.
    Steps:
    1. Convert to grayscale (removes color distractions)
    2. Apply Gaussian blur (smooths noise)
    3. Apply adaptive thresholding (enhances text contrast)
    """

    # Convert image to grayscale (reduces unnecessary color details)
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    # Apply Gaussian Blur to smooth noise while keeping text sharp
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Adaptive Thresholding to enhance text visibility
    processed = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 11, 2)

    return processed


# def extract_text_from_pdf(pdf_bytes):
#     """
#     Converts a PDF file into images, preprocesses them, 
#     and extracts text using OCR.
    
#     Returns extracted text as a list of strings (one per page).
#     """

#     # Convert the PDF file (in bytes) into a list of images (one per page)
#     images = convert_from_bytes(pdf_bytes)

#     extracted_text = []  # Store text from each page

#     for img in images:
#         # Preprocess the image (improve OCR accuracy)
#         processed_img = preprocess_image(img)

#         # Extract text using Tesseract OCR
#         text = pytesseract.image_to_string(processed_img)
        
#         # Store extracted text for this page
#         extracted_text.append(text)

def extract_text_from_pdf(pdf_data):
    """Extract text from a PDF file using OCR."""
    
    # Convert PDF to a list of images (one per page)
    images = convert_from_bytes(pdf_data)

    # Extract text from each image and join them into a single string
    extracted_text = "\n".join(pytesseract.image_to_string(image) for image in images)



    return extracted_text  # Return text from all pages
