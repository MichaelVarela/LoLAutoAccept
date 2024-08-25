import pyautogui, time
from send_text import textPhone


while True:
    try:
        location = pyautogui.locateCenterOnScreen('accept_images/large_accept.PNG', confidence=0.5)
        break
    except:
        try:
            location = pyautogui.locateCenterOnScreen('accept_images/medium_accept.PNG', confidence=0.5)
            break
        except:
            try:
                location = pyautogui.locateCenterOnScreen('accept_images/small_accept.PNG', confidence=0.5)
                break
            except:
                try:
                    location = pyautogui.locateCenterOnScreen('accept_images/real_accept.PNG', confidence=0.5)
                    break
                except:
                    time.sleep(1)
                    print('slept')

pyautogui.moveTo(location)
pyautogui.click()

textPhone()