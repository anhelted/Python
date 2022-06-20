import ascii_magic
import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('x',help='Input Image Path!',type=str)

    arg = parser.parse_args()
    path = arg.x

    my_art = ascii_magic.from_image_file(path)
    ascii_magic.to_terminal(my_art)
except Exception as e:
    print('Path Error!',e)

"""
How to use this program
type on your terminal :
python img2ascii.py (filename.format) 
"""
