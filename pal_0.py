##############################################################################
# File:         pal_0.py                                                     #
# Author:       Tom Gorbett                                                  #
# Last Updated: 2021-06-09                                                   #
# Description:  This script is meant to be automated with the hotkey of      #
#               Ctrl + Alt + 0. When pressed, this script will generate and  #
#               set a new desktop background, with a color pallete of 2 to 5 #
#               randomly chosen hexcodes. This script also enters in a       #
#               grade of 0 into the pal_log file for the previous desktop    #
#               background, entering the new image's details on a new line.  #
##############################################################################

import datetime
import random
import uuid
import ctypes
from PIL import Image, ImageDraw

def rgb_to_hex(red, green, blue):
    return '#%02x%02x%02x' % (red, green, blue)
# This is a function used to convert base-10 RGB values to base-15 hexcodes.

grade = 0  # This is the grade for the previous image
uid = uuid.uuid1()  # Here we generate a unique ID for the pal_log file.
i = 0
colors = int(random.uniform(2, 5))  # The color pallet contains 2 to 5 colors.
hexes = []
hex_limits = [0,255,0,255,0,255,0,255,0,255]
image_path = "C:/Users/gorbetw/Pictures/pal/pal.png"
pic_dim = [1920,1080]  # This tells us the dimensions of the entire image.
square_dim = [120,120]  # This tells us the dimensions of the square.
x0 = x1 = square_dim[0] / 2 - 1
y0 = 0
y1 = wid = square_dim[1]
# The previos three lines set coordinates for where the square begins.
    
while i < colors * 2:
    hexes.append(
        rgb_to_hex(int(random.uniform(hex_limits[i], hex_limits[i + 1])),
		   int(random.uniform(hex_limits[i], hex_limits[i + 1])),
		   int(random.uniform(hex_limits[i], hex_limits[i + 1]))
    ))
    i += 2
# This operation creates the hexcodes for each color.

im = Image.open(image_path)
draw = ImageDraw.Draw(im)
# Here we use the old image as a template for the new one.

while y0 <= pic_dim[1]:
    draw.line([(x0, y0), (x1, y1)],
              fill=hexes[int(random.uniform(0,colors))],
              width=wid)
    x0 += wid
    x1 += wid
    # This moves the pointer over for the next square
    if x0 > pic_dim[0]:
        x0 = x1 = square_dim[0] / 2 - 1
        y0 += square_dim[1]
        y1 += square_dim[1]
    # This moves the cursor to the next row, if we've reached the end.

im.save(image_path) # We save over the old image.

nulls = ["null"] * (5 - len(hexes))
hex_string = str(hexes + nulls)
# If there's less than five hexcodes, we populate the blanks with "null"

drop_char = "'[] "
for char in drop_char:
    hex_string = hex_string.replace(char,"")
# We remove a few characters from the string to populate the log file

with open("C:/Users/gorbetw/Pictures/pal/pal_log.csv", 'a') as file:
    file.write(
        str(grade) + '\n'
        + str(uid) + ',' 
        + hex_string + ','
        + str(datetime.datetime.now()) + ','
    )
# This is where we populate the grade, then the new image details

ctypes.windll.user32.SystemParametersInfoW(20,
                                           0,
                                           image_path,
                                           0)
# Even though it's the same file, we need to reset the desktop background.
