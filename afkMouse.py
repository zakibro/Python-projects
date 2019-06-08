#! python3

import pyautogui
import time

while True:
    try:
        pyautogui.moveRel(10, 0, duration=0.25)
        pyautogui.moveRel(-10, 0, duration=0.25)
        time.sleep(10)
    except KeyboardInterrupt:
        print('Breaking the loop!')
        break
