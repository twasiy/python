# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread("/home/wasiy/Pictures/vault/tanha_emon.jpeg")

# # Convert to grayscale (optional)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply Gaussian blur
# blurred = cv2.GaussianBlur(gray, (0, 0), 3)

# # Sharpening filter
# sharpened = cv2.addWeighted(gray, 1.5, blurred, -0.5, 0)

# # Save and show
# output_path = "/home/wasiy/Documents/sharpened_image.jpg"
# cv2.imwrite(output_path, sharpened)

# print(f"Sharpened image saved at: {output_path}")



# import numpy as np
# import cv2
# from skimage import io, restoration, color, img_as_ubyte

# # Load the image
# image_path = "/home/wasiy/Pictures/vault/tanha_emon.jpeg"
# image = io.imread(image_path)

# # Convert to grayscale (Wiener filter works best on grayscale images)
# image_gray = color.rgb2gray(image)

# # Create a Point Spread Function (PSF) - Simulates the blur effect
# psf = np.ones((7, 7)) / 49 # Adjust size for different blur levels

# # Apply Wiener filter for deblurring
# deblurred = restoration.wiener(image_gray, psf, balance=0.1)

# # Convert back to 8-bit format for saving
# deblurred = img_as_ubyte(deblurred)

# # Save the deblurred image
# output_path = "/home/wasiy/Documents/deblurred_image.jpg"
# cv2.imwrite(output_path, deblurred)

# print(f"Deblurred image saved at: {output_path}")

