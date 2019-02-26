#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

import pyautogui
from PIL import Image

pyautogui.PAUSE = 1
"""
Point(x=95, y=191)
Point(x=559, y=431)

print(first)
print(last)
pyautogui.moveTo(first)
pyautogui.moveTo(last)
"""

def getFirstLast():
   try:
      listBlocks = list(pyautogui.locateAllOnScreen('images/oneBlock.png'))
      first = pyautogui.center(listBlocks.__getitem__(0))
      last = pyautogui.center(listBlocks.__getitem__((listBlocks.__len__())-1))
   except:
      return (0,0),(0,0)
      pass
   return first, last


"""
   print(pixel_value)
   print(im.size)

"""

def getColorPixel(imageName='oneBlock'):
   im = Image.open('images/'+ imageName + '.png', 'r')
   width, height = im.size
   pixel_value = im.getdata().getpixel((8,8))
   return pixel_value


