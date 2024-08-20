import pyautogui
import time
from send_text import textPhone


while True:
    try:
        location = pyautogui.locateCenterOnScreen('accept_pic.PNG', confidence=0.7)
        break;
    except:
        time.sleep(1)
        print('slept')

pyautogui.moveTo(location)
pyautogui.click()

textPhone()