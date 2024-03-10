import time
import pandas
import pyautogui

#PASSO 1 - Acessar site:
pyautogui.PAUSE = 0.5
#apertar tecla windows
pyautogui.press("win")
#digitar nome do programa a abrir
pyautogui.write("google")
#apertar enter
pyautogui.press("enter")
#acessar controle de estoque
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#esperar 5 seg
time.sleep(2)

#PASSO 2 - Fazer Login:

#Clicar no campo
pyautogui.click(x=254, y=367)
#digitar e-mail
pyautogui.write("email@email.com")
#apertar tab
pyautogui.press("tab")
#digitar senha
pyautogui.write("pipoca123")
#apertar enter
pyautogui.press("enter")
time.sleep(2)

#PASSO 3 - Importar DB:

tabela = pandas.read_csv("produtos.csv")

#Passo 4 - Cadastrar produto


#escrever codigo

for linha in tabela.index:

    pyautogui.click(x=240, y=265)

# inserir codigo
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
# inserir marca
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
# inserir produto
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
# inserir categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
# inserir preco
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
# inserir custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
# inserir observacao
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha,"obs"]))

    pyautogui.press("enter")

