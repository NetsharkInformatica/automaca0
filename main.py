import pyautogui as p
import time


# pyautogui.press('win')
# pyautogui.PAUSE=1
# pyautogui.write('chrome')
# pyautogui.press('enter')
# pyautogui.write('heliotome.com.br')
# pyautogui.press('enter')
#print(p.position())
p.hotkey('win','r')
p.sleep(1)
p.typewrite('notepad')
p.sleep(2)
p.press('enter')
p.sleep(2)
p.typewrite('ola, eu sou um bot')
p.sleep(3)
p.hotkey('ctrl','s')
p.sleep(3)
p.typewrite('teste.txt')
p.sleep(2)
p.press('enter')
p.sleep(3)
p.hotkey('alt','F4')
