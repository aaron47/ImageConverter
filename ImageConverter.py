import argparse
import os
from PIL import Image


class ImageConverter:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description="Script to convert your image from its current format to your desired format")
        parser.add_argument("--img_path", type=str, help="The path to your image")
        parser.add_argument("--new_ext", type=str, help="Your desired new extension if not provided, the script assumes you're trying to convert from a JPG to a PNG", required=False)
        parser.add_argument("--delete_original", action="store_true", help="Whether to remove the old image or not")

        args = parser.parse_args()
        self.input_img_path: str = args.img_path
        self.new_extension: str = args.new_ext
        self.delete_original: bool = args.delete_original

    def convert(self) -> None:
        if not os.path.exists(self.input_img_path):
            print(f"The file {self.input_img_path} does not exist.")
            return

        with Image.open(self.input_img_path) as img:
            output_file: str = os.path.splitext(self.input_img_path)[0]
            
            if self.new_extension:
                img.save(f"{output_file}.{self.new_extension}")
            else:
                img.save(f"{output_file}.png")

            if self.delete_original:
                os.remove(self.input_img_path)


if __name__ == "__main__":
    ImageConverter().convert()
