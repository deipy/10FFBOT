import pyautogui
import time
import pytesseract

x,y,w,h =652,220,454,149

def TabEnter():
    pyautogui.keyDown('tab')
    pyautogui.press('enter')
    pyautogui.keyUp('tab')

def AntiCheat():
    image = pyautogui.screenshot(region=(x,y,w,h))
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\TesseractOCR\tesseract.exe'
    image.save("C:\\Users\\arthu\Pictures\FFCAPTURE.jpg")
    time.sleep(0.2)
    to_type = pytesseract.image_to_string(r"C:\Users\arthu\Pictures\FFCAPTURE.jpg")
    to_type = to_type[:-1]+" "
    pyautogui.typewrite(to_type, 0)
    time.sleep(0.5)
    TabEnter()

time.sleep(5)
pyautogui.click()
time.sleep(1.5)
AntiCheat()