#!/bin/bash

# Define the API endpoint (update to /extract-text)
API_URL="http://127.0.0.1:5000/extract-text"

# Define the file to test
FILE_PATH="Curriculum_Vitae.pdf"

# Send a POST request using curl
curl -X POST -F "file=@$FILE_PATH" $API_URL