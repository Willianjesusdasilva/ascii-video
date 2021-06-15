import cv2
import numpy as np
import pyautogui
import os
from io import StringIO

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def img_to_ascii(image):
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    height, width = image.shape
    height = height//3
    width = width//2
    image_resized = cv2.resize(image, (width, height)) 
    buff = StringIO()
    for line in image_resized:
        buff.write("".join([ASCII_CHARS[pixel//25] for pixel in line])+"\n")
    
    return buff

while True:
    image = pyautogui.screenshot(region=(550,529, 200,170))
    result = img_to_ascii(cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY))
    os.system('cls')
    print(result.getvalue())

