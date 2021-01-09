import pyautogui
import webbrowser
import time
import pytesseract

#x=533
#y=203
#w=787
#h=39

x,y,w,h=533,203,787,39   #Position and scale for anti-cheat
#x,y,w,h =652,220,454,149 #position and scale for normal tes


def openUrl():
    webbrowser.open("https://www.10fastfingers.com/typing-test/english", new=2)
    pyautogui.moveTo(68, 249)
    time.sleep(0.5)
    pyautogui.click()

def ReadNType():
    image = pyautogui.screenshot(region=(x,y,w,h))
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\TesseractOCR\tesseract.exe'
    image.save("C:\\Users\\arthu\Pictures\FFCAPTURE.jpg")
    time.sleep(0.1)
    to_type = pytesseract.image_to_string(r"C:\Users\arthu\Pictures\FFCAPTURE.jpg")
    to_type = to_type[:-1]+" "
    pyautogui.typewrite(to_type, 0)

openUrl()
time.sleep(1)
started_at = time.time()
while time.time()-started_at <=60:
    ReadNType()