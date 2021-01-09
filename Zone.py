import pyautogui

while True:
    x,y, = pyautogui.position()
    print("pos : "+str(x)+"; "+str(y))