#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

import pyautogui
import initializer

first, last = initializer.getFirstLast()

colorBlank = initializer.getColorPixel("oneBlock") 

colorN1 = initializer.getColorPixel('number1') 

colorN2 = initializer.getColorPixel('number2') 

colorN3 = initializer.getColorPixel('number3') 

colorN4 = initializer.getColorPixel('number4') 


if first == last:
    print('you''re not in the game')
    exit()

print('still there, here we go!')


def upleft(pos):
    return pos.x-16, pos.y-16

def up(pos):
    return pos.x, pos.y-16

def upright(pos):
    return pos.x+16, pos.y-16

def left(pos):
    return pos.x-16, pos.y

def right(pos):
    return pos.x+16, pos.y
    
def downleft(pos):
    return pos.x-16, pos.y+16

def down(pos):
    return pos.x, pos.y+16

def downright(pos):
    return pos.x+16, pos.y+16


def countBlankAround(pos, im):

    color = colorBlank

    colors = (
        im.getpixel(upleft(pos)),   #1
        im.getpixel(up(pos)),       #2
        im.getpixel(upright(pos)),  #3
        im.getpixel(left(pos)),     #4
        im.getpixel(right(pos)),    #5
        im.getpixel(downleft(pos)), #6
        im.getpixel(down(pos)),     #7
        im.getpixel(downright(pos)) #8
    )
    number = 0
    for colorPix in colors:
        if(color == colorPix):
            number = number + 1
            
    return number, colors

def getColorPixel(pos, im = pyautogui.screenshot()):

    return im.getpixel(pos)


pos = downright(first)

pyautogui.click(pos)

im = pyautogui.screenshot()

number, colors = countBlankAround(pyautogui.position(), im)
print(number)






    
"""
pyautogui.PAUSE = 2.5
im = pyautogui.screenshot()

pyautogui.moveTo(
    pyautogui.center((
        pyautogui.locateOnScreen('oneBlock.png')
    ))
)

print('num1')
colorN1 = im.getpixel((
    pyautogui.center((
        pyautogui.locateOnScreen('number1.png')
    ))
)))

print('num2')
colorN2 = im.getpixel((
    pyautogui.center((
        pyautogui.locateOnScreen('number2.png')
    ))
)))

print('num3')
colorN3 =
num4 = 0,0,123
print(num4);
"""