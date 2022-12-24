import datetime
import os
from io import BytesIO

import cv2
import numpy as np
import requests
from PIL import Image

def convert_image_to_sketch(image, gaussian_kernel):
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert_grey = cv2.bitwise_not(grey_image)
    gaussian_blur = cv2.GaussianBlur(invert_grey, (gaussian_kernel,gaussian_kernel), 0)
    invert_blur = cv2.bitwise_not(gaussian_blur)    
    sketch = cv2.divide(grey_image, invert_blur, scale=256.0)

    return sketch

def get_unique_file_name():
    unique_number = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"image_{unique_number}.png"

def get_image_from_url(url):
    """
    Download image from url, convert color
    """
    image_data = Image.open(BytesIO(requests.get(url).content))
    image = np.array(image_data)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    return image

def save_image(image,  file_name=None, path=""):
    if not file_name:
        file_name = get_unique_file_name()

    file_path = os.path.join(path, file_name)
    print(f"Saving image at: {file_path}")
    cv2.imwrite(file_path, image)
