import click
import cv2
import requests
import numpy as np
from io import BytesIO
from PIL import Image
import datetime
import os

GAUSSIAN_KERNEL = 21
PATH = "/Users/changikchoi/Documents/Github/coloring_book/assets/chromedriver" 
INPUT_IMAGE_PATH = "input_images"
OUTPUT_IMAGE_PATH = "output_images" 

def convert_image_to_sketch(image):
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_image)
    gaussian_blur = cv2.GaussianBlur(invert, (GAUSSIAN_KERNEL,GAUSSIAN_KERNEL), 0)
    invert_blur = cv2.bitwise_not(gaussian_blur)    
    sketch = cv2.divide(grey_image, invert_blur, scale=256.0)

    return sketch

def get_image_from_url(url, file_name=None):
    """
    Download image from url, convert color
    """
    image_data = Image.open(BytesIO(requests.get(url).content))
    image = np.array(image_data)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if not file_name:
        unique_number = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file_name = f"image_{unique_number}"
    file_path = os.path.join(INPUT_IMAGE_PATH, file_name)
    # save file
    cv2.imwrite(file_path, image)

    return file_name, image

@click.command()
@click.option(
    "--key_word",
    "-kw", 
    default="test.jpg",
    show_default=True,
    help="Type keyword to serach image"   
)
def main(key_word):
    url = "https://cdn.shopify.com/s/files/1/0363/6127/3479/products/pp-img-plush_medium-huggy_wuggy-1-front_1000x.jpg?v=1659727820"
    file_name, image = get_image_from_url(url)
    sketch = convert_image_to_sketch(image)
    output_file_path = os.path.join(OUTPUT_IMAGE_PATH, file_name)
    cv2.imwrite(output_file_path, sketch)

if __name__ == "__main__":
    main()