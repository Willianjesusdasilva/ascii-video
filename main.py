import cv2
import numpy as np
import pyautogui
import os

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.05

def img_to_ascii(image):
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    height, width = image.shape
    height = height//2
    width = width//2
    ratio = height/width
    new_height = int(width * ratio)
    image_resized = cv2.resize(image, (width, new_height)) 
    characters = []
    for line in image_resized:
        characters.append("".join([ASCII_CHARS[pixel//25] for pixel in line])+"\n")

    return ''.join(characters)

while True:
    image = pyautogui.screenshot(region=(552,537, 200,170))
    result = img_to_ascii(cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY))
    os.system('cls')
    print(result)

