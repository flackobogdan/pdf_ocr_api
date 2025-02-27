# app.py

import os
from flask import Flask, request, jsonify
from config import ALLOWED_EXTENSIONS
from utils import allowed_file
from ocr_utils import extract_text_from_pdf

# Initialize Flask app
app = Flask(__name__)

@app.route('/extract-text', methods=['POST'])
def extract_text():
    """
    Flask API endpoint:
    - Accepts a PDF file via POST request
    - Converts PDF to images
    - Preprocesses each image
    - Runs OCR (Tesseract) on images
    - Returns extracted text in JSON format
    """

    # Check if file exists in request
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    # Check if file has a name
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Validate file extension
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    try:
        # Extract text from the PDF file
        extracted_text = extract_text_from_pdf(file.read())

        # Return extracted text as JSON
        return jsonify({'extracted_text': extracted_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
