#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys 
import sys

"""
Color Pallete Extractor 
v1.0.0
"""

image_path = sys.argv[1]
ct = ColorThief(image_path)
dominant_color = ct.get_color(quality=1)

plt.imshow([dominant_color])
plt.show()

palette = ct.get_palette(color_count=5)
plt.imshow([[ palette[i] for i in range(5) ]])
plt.show()

for color in palette:
    print(color)
    print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
    print(colorsys.rgb_to_hsv(*color))
    print(colorsys.rgb_to_hls(*color))



