# import cv2
# import numpy as np
from PIL import Image, ImageDraw, ImageFont

def text_to_handwriting(text, output_filename="handwriting.png"):
    img = Image.new("RGB", (800, 400), "white")
    draw = ImageDraw.Draw(img)
    
    # Change the font path to an actual handwriting-style font
    font_path = 'Arial.ttf' # Replace with a handwriting font file
    font = ImageFont.truetype(font_path, 30)
    
    draw.text((50, 50), text, fill="black", font=font)
    img.save(output_filename)
    img.show()

text_to_handwriting("Hello, this is a handwriting test!")
