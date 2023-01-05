import pyautogui
from time import sleep
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def abrir_o_navegador():
    sleep(2)
    pyautogui.press('winleft')
    sleep(2)
    pyautogui.write('opera')
    sleep(2)
    pyautogui.press('enter')
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def abrir_planilha_de_saldos():
    worksheet = 'docs.google.com/spreadsheets/d/1T1V3hTCkhLT8k55JTcEj9keHFtfyNQtE4W1VGaRoFRQ/edit#gid=0'
    pyautogui.write(worksheet)
    sleep(3)
    pyautogui.press('enter')
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def atualizar_pagina():
    pyautogui.press('f5')
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def abrir_relatorio_do_orçamento():
    pyautogui.write("https://docs.google.com/spreadsheets/u/1/") #clique para abrir todas as planilhas
    sleep(3)
    pyautogui.press("enter")
    sleep(3)
    pyautogui.click(x=347, y=120)  
    sleep(3)
    pyautogui.press("tab")
    sleep(3)
    pyautogui.write("Relatório do orçamento") #digitar Relatório do orçamento
    sleep(3)
    pyautogui.press("down")
    pyautogui.press("down")
    sleep(3)
    pyautogui.press("enter")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def editar_relatorio_do_orçamento():
    pyautogui.keyDown('ctrl')
    pyautogui.press('h')
    pyautogui.keyUp('ctrl')
    sleep(3)
    pyautogui.write('--')
    sleep(3)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.press('tab')
    sleep(3)
    pyautogui.write('0,00')
    sleep(3)
    for _ in range(10):                                         
        pyautogui.press('tab')
    sleep(3)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.press('tab')
    sleep(3)
    pyautogui.press('enter')
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def fechar_navegador():
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def atualizar_dados_da_planilha():
    abrir_o_navegador()
    sleep(8)
    abrir_planilha_de_saldos()
    sleep(7)
    atualizar_pagina()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def updatedb():
    abrir_o_navegador()
    sleep(3)
    abrir_relatorio_do_orçamento()
    sleep(3)
    editar_relatorio_do_orçamento()
    sleep(1)
    fechar_navegador()
    sleep(3)
    abrir_o_navegador()
    sleep(8)
    abrir_planilha_de_saldos()
    sleep(7)
    atualizar_pagina()
    sleep(2)
    fechar_navegador()
