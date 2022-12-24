import click
from utils import convert_image_to_sketch, get_image_from_url, save_image
import customtkinter
import tkinter

GAUSSIAN_KERNEL = 21
INPUT_IMAGE_PATH = "input_images"
OUTPUT_IMAGE_PATH = "output_images" 

@click.command()
@click.option(
    "--key_word",
    "-kw", 
    default="test.jpg",
    show_default=True,
    help="Type keyword to serach image"   
)
def main(key_word):
    url ="https://ae01.alicdn.com/kf/Sdbe385c5d33d4d0eafab35161f26187f7/Rainbow-Friends-Plush-Game-Doll-Blue-Yellow-Monster-Long-Hand-Monster-Soft-Stuffed-Animal-Halloween-Christmas.jpg_Q90.jpg_.webp"
    input_image = get_image_from_url(url)
    sketch_image = convert_image_to_sketch(input_image, gaussian_kernel=GAUSSIAN_KERNEL)
    # save input image
    save_image(input_image, path=INPUT_IMAGE_PATH)
    # save output image
    save_image(sketch_image, path=OUTPUT_IMAGE_PATH)

if __name__ == "__main__":
    main()
    