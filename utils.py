import datetime
import os
from io import BytesIO

import cv2
import numpy as np
import requests
from PIL import Image

def convert_image_to_sketch(image, gaussian_kernel):
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_image)
    gaussian_blur = cv2.GaussianBlur(invert, (gaussian_kernel,gaussian_kernel), 0)
    invert_blur = cv2.bitwise_not(gaussian_blur)    
    sketch = cv2.divide(grey_image, invert_blur, scale=256.0)

    return sketch

def get_image_from_url(url, file_name=None, input_path="input_images"):
    """
    Download image from url, convert color
    """
    image_data = Image.open(BytesIO(requests.get(url).content))
    image = np.array(image_data)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if not file_name:
        unique_number = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file_name = f"image_{unique_number}"
    file_path = os.path.join(input_path, file_name)
    # save file
    cv2.imwrite(file_path, image)

    return file_name, image

def save_sketch_image(image,  file_name, output_path="output_images"):
    output_file_path = os.path.join(output_path, file_name)
    cv2.imwrite(output_file_path, image)
