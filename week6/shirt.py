# expects 2 command-line arguments 1 JPG/JPEG/PNG (case insensitive) as input and one as output(both must be the same type)
# open input(Image.open), crop&resize(ImageOps.fit), overlay(Image.paste), save(Image.save)
# exit if !=2 command-line arguments, arguments have wrong format, input dont exist, input&output different format
# determine file extension via os.path.splitext
import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    check_input()
    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as file:
            updated_image = ImageOps.fit(file, shirt.size)
            updated_image.paste(shirt, shirt)
            updated_image.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


def check_input():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        valid_extensions = [".jpg", ".jpeg", ".png"]
        ext_1 = splitext(sys.argv[1])[1].lower()
        ext_2 = splitext(sys.argv[2])[1].lower()
        if ext_1 not in valid_extensions:
            sys.exit("Invalid output")
        elif ext_1 != ext_2:
            sys.exit("Input and output have different extensions")


main()