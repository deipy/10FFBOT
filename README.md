# 10FF BOT
This script takes a screenshot of the typing test at https://www.10fastfingers.com/typing-test/english, reads the text from the image and types it as fast as possible,
just for fun

# Uses
use 10fastfingers.py on the main website, AntiCheat.py to defeat the anti-cheat, and Zone.py to recalculate the coordinates of the regions to screenshot and read.
you might need to change the filepaths for where to save the image, as well as the region to screenshot (use the zones.py script to get the pixel coordinates of corners, then subtract to get width and height of region, change x,y,w and h variables accordingly. Default variables are for a firefox zoomed out 80%

# Requirements
This script requires pyautogui, webbrowser, time and pytesseract


# Performance Notes
The script acheived max performance, 355wpm but was limited by the website itself, and achieved 1440wpm on the anti-cheat (which ultimately got the account banned :( )
