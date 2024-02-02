import pyautogui, webbrowser 
from time import sleep 


webbrowser.open('https://web.whatsapp.com/send?phone=+NumberHere')

sleep(10)

for i in range(5): 
     pyautogui.typewrite('./img.jpg')
     pyautogui.press('enter') 
