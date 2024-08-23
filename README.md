<<<<<<<<<<<<<<  ✨ Codeium Command ⭐  >>>>>>>>>>>>>>>>
# QR Code Generator

A simple QR code generator built with Flask.

## How to use

1. Go to the website and enter the text you want to encode in the input field.
2. Click the "Generate" button.
3. The QR code will appear below the input field.

## How it works

The website uses the Flask web framework to create a simple web interface. The QR code is generated using the qrcode library. When the user clicks the "Generate" button, the website sends a POST request to the server with the text the user entered. The server then generates the QR code and sends it back to the user as a PNG image.

## How to run

1. Install the necessary packages with pip install -r requirements.txt
2. Run the website with python app.py
3. Go to http://localhost:5001 in your web browser to see the website.



