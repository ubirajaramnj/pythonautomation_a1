import pyautogui
import time

pyautogui.PAUSE = 0.5

#pyautogui.click('win')
#pyautogui.hotkey('cmd', 'space')
pyautogui.keyDown("command")
pyautogui.press("space")
pyautogui.keyUp("command")

pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

pyautogui.position(x=924, y=443)
pyautogui.hotkey('command', 'a')
pyautogui.write('pythonimpressionador@gmail.com')

#pyautogui.position(x=887, y=547) #Caso tivesse que pegar o campo senha 
pyautogui.press('tab')
pyautogui.write('XyZ#321')
time.sleep(3)

import pandas
tabela = pandas.read_csv('produtos.csv')

pyautogui.click(x=1713, y=100)
pyautogui.write('')

pyautogui.press('tab')
pyautogui.write('')

pyautogui.press('tab')
pyautogui.write('')

pyautogui.press('tab')
pyautogui.write('')

pyautogui.press('tab')
pyautogui.write('')

pyautogui.press('tab')
pyautogui.write('')

pyautogui.press('tab')
pyautogui.write('')

pyautogui.press('tab')
pyautogui.press('enter')




print(tabela)