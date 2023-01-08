#############################
# File:         drizzle.py  #
# Author:       Tom Gorbett #
# Last Updated: 2022-01-15  #
#############################

import ctypes
import random
import uuid
from PIL import Image, ImageDraw

im_path = "C:/Users/gorbetw/Pictures/rain/rain.png"
i = 0
hexes = []
colors = int(random.uniform(2, 5))  # The number of colors in the pallet
hex_limits = [0,128]
bg_limits = [128,256]
drops = int(random.uniform(20, 100))
drop_limits = [20,100]
uid = uuid.uuid1()  # Here we generate a unique ID for the rain_log file.

# This is a function used to convert base-10 RGB values to base-15 hexcodes.
def rgb_to_hex(red, green, blue):
    return '#%02x%02x%02x' % (red, green, blue)

# Here we use the old image as a template for the new one.
im = Image.open(im_path)
r = int(random.uniform(bg_limits[0],bg_limits[1]))
g = int(random.uniform(bg_limits[0],bg_limits[1]))
b = int(random.uniform(bg_limits[0],bg_limits[1]))
im.paste((r,g,b), [0,0,im.size[0],im.size[1]])

while i <= colors:
    hexes.append(
        rgb_to_hex(int(random.uniform(hex_limits[0], hex_limits[1])),
		   int(random.uniform(hex_limits[0], hex_limits[1])),
		   int(random.uniform(hex_limits[0], hex_limits[1]))
    ))
    i += 1
i = 0
# This operation creates the hexcodes for each color.

draw = ImageDraw.Draw(im)
while i <= drops:
    x = int(random.uniform(0,im.size[0]))
    y0 = int(random.uniform(0,im.size[1]))
    y1 = y0 + int(random.uniform(drop_limits[1]/5, drop_limits[1]))
    draw.line([(x, y0), (x, y1)],
              fill=hexes[int(random.uniform(0,colors))],
              width=int(random.uniform(drop_limits[0]/5, drop_limits[0])))
    i += 1

im.save(im_path) # We save over the old image.

ctypes.windll.user32.SystemParametersInfoW(20,
                                           0,
                                           im_path,
                                           0)
# Even though it's the same file, we need to reset the desktop background.