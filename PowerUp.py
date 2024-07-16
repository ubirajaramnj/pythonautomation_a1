import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')
#pyautogui.hotkey('cmd', 'space')
#pyautogui.keyDown("command")
#pyautogui.press("space")
#pyautogui.keyUp("command")

pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=793, y=391)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('pythonimpressionador@gmail.com')

pyautogui.press('tab')
pyautogui.write('XyZ#321')

pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

import pandas as pd
produtos = pd.read_csv('produtos.csv')

for _, item in produtos.iterrows():
    pyautogui.click(x=889, y=277)
    pyautogui.write(item['codigo'])
    
    pyautogui.press('tab')
    pyautogui.write(item['marca'])

    pyautogui.press('tab')
    pyautogui.write(item['tipo'])

    pyautogui.press('tab')
    pyautogui.write(str(item['categoria']))

    pyautogui.press('tab')
    pyautogui.write(str(item['preco_unitario']))

    pyautogui.press('tab')
    pyautogui.write(str(item['custo']))

    pyautogui.press('tab')
    pyautogui.write(str(item['obs']))

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)

    time.sleep(5)