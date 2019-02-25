#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

import pyautogui

pyautogui.PAUSE = 2.5
im = pyautogui.screenshot()

pyautogui.moveTo(
    pyautogui.center((
        pyautogui.locateOnScreen('oneBlock.png')
    ))
)

print('num1')
num1 = im.getpixel((
    pyautogui.center((
        pyautogui.locateOnScreen('number1.png')
    ))
)))

print('num2')
num2 = im.getpixel((
    pyautogui.center((
        pyautogui.locateOnScreen('number2.png')
    ))
)))

print('num3')
num3 = im.getpixel((
    pyautogui.center((
        pyautogui.locateOnScreen('number3.png')
    ))
)))
num4 = 0,0,123
print(num4);




"""



import sys
def better_version_of_yourself(inicial=1.01, limit=365):
    i=2
    vet = [inicial]
    while i<=limit:
        vet.append(vet[i-2]*vet[0])
        i+=1
    return(str(inicial) + '^' + str(limit) + '= %.3f' % vet[limit-1] + '; ')
print('\n   ' + better_version_of_yourself(1.001))
print('   ' + better_version_of_yourself(0.999) + '\n')



codigo cru:
#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

import sys
def better_version_of_yourself(inicial=1.01, limit=365, cont=4):
    i=2
    vet = [inicial]
    
    string = str(inicial) + '^1= %.3f' % vet[0] + '; '

    while i<=limit:
        vet.append(vet[i-2]*vet[0])
        #print(' ', i, ': %.2f' % vet[i])
        string += str(inicial) + '^' + str(i) + '= %.3f' % vet[i-1] + '; '  
        if i%cont==0:
            string += '\n'
        i+=1
    #print(string)
    return(str(inicial) + '^' + str(limit) + '= %.3f' % vet[limit-1] + '; ')

print(' ')
print('   ' + better_version_of_yourself(1.001))
print('   ' + better_version_of_yourself(0.999))
print(' ')"""
