# Watermark Processor

Watermark Processor is a simple Python application that allows users to add text and logo watermarks to images. The application is built using Tkinter for the GUI and Pillow for image processing.

## Features

- Open an image file and display it.
- Add a text watermark to the image.
- Add a logo watermark to the image.
- Save the watermarked image.
- Customize the font color of the text watermark.

## Requirements

- Python 3.x
- Tkinter
- Pillow

## Installation

1. Clone the repository or download the source code.

    ```bash
    git clone https://github.com/Black-Scorpio/custom-water-mark.git
    
    pip install pillow
    
    python main.py

## Usage
2. Use the buttons to perform the following actions:
- Open Image: Open an image file to add watermarks.
- Enter watermark text here: Input the text for the watermark.
- Add Text Watermark: Add the text watermark to the image.
- Add Logo Watermark: Open a logo file to add as a watermark to the image.
- Save Image: Save the watermarked image to a file.

## Customization
- You can change the default font color by modifying the self.font_color attribute in the WatermarkProcessor class.
- The font file used for the text watermark is static/PlaywriteFRModerne-Thin.ttf. You can replace this with any other font file by updating the path in the add_text_watermark method.