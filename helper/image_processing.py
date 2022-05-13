
from pathlib import Path
import imghdr
import os
from PIL import Image

def image_rename(imgs_path):
    data_dir = imgs_path
    image_extensions = [".png", ".jpg", "jpeg"]  # add there all your images file extensions

    img_type_accepted_by_tf = ["bmp", "gif", "png"]
    for filepath in Path(data_dir).rglob("*"):
        if filepath.suffix.lower() in image_extensions:
            img_type = imghdr.what(filepath)
        if img_type is None:
            print(f"{filepath} is not an image")
            continue
        elif img_type in image_extensions:
            continue
        print(f"{filepath} is a {img_type}, not accepted by TensorFlow")
        # file_rename = str(filepath).split("\\")[-1]
        file_rename = filepath
        pre, ext = os.path.splitext(file_rename)
        
        # importing the image 
        im = Image.open(file_rename)

        # converting to jpg
        rgb_im = im.convert("RGB")

        # exporting the image
        rgb_im.save(pre + ".jpg")
        if ".jpg" not in str(file_rename):
            os.remove(file_rename)