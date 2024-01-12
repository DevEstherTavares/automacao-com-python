##PASSO A PASSO - POJETO DE AUTOMAÇÃO - SUBIR BASE DE DADOS PARA SISTEMA##
##--------------Jornada de python com HASHTAG PROGRAMAÇÃO---------------##

# Bibliotecas utilizadas: pyautogui, time
import pyautogui # biblioteca para controlar o mouse e teclado
import time # biblioteca para controlar o tempo

# Passo 1: Entrar no sistema da empresa #
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 3 # tempo de espera entre cada ação

# Abrir o navegador
pyautogui.press("win") # tecla windows
pyautogui.write("chrome") # escrever o nome do navegador
pyautogui.press("enter") # carregar o navegador

# Entrar no sistema pelo link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link) # escrever o link
pyautogui.press("enter") # carregar a página
time.sleep(5) # tempo de espera para carregar a página

# Passo 2: Fazer o login no sistema #

# selecionar o campo de email
pyautogui.click(x=430, y=412) # localização do campo de email (adicione sua localização usando o auxiliar.py)
pyautogui.write("esther.esther@teste.com") # escrever seu email

# selecionar o campo de senha
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha") # escrever sua senha
pyautogui.press("enter") # apertar enter para entrar no sistema
time.sleep(5) # tempo de espera para carregar a página

import pandas as pd # biblioteca para trabalhar com arquivos excel

# Passo 3: Importar a base de produtos pra cadastrar
tabela = pd.read_csv("produtos.csv") 
print(tabela) # exibir a tabela

# Passo 4: Cadastrar os produtos
for linha in tabela.index:
    pyautogui.click(x=423, y=291) # clicar no botão de adicionar produto
    codigo = tabela.loc[linha, "codigo"] # atribuir a variável código o valor da coluna código
    pyautogui.write(str(codigo)) # escrever o código do produto
    pyautogui.press("tab") # passar para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "marca"])) # escrever a marca do produto
    pyautogui.press("tab") # passar para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "tipo"])) # escrever o tipo do produto
    pyautogui.press("tab") # passar para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "categoria"])) # escrever a categoria do produto
    pyautogui.press("tab") # passar para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) # escrever o preço do produto
    pyautogui.press("tab") # passar para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "custo"])) # escrever o custo do produto
    pyautogui.press("tab") # passar para o próximo campo
    obs = tabela.loc[linha, "obs"] # atribuir a variável obs o valor da coluna obs
    if not pd.isna(obs): # se a variável obs não for vazia
        pyautogui.write(str(tabela.loc[linha, "obs"])) # escrever a obs do produto
    pyautogui.press("tab") # passar para o próximo campo
    pyautogui.press("enter") # apertar enter para salvar o produto
    pyautogui.scroll(5000) # rolar a página para baixo







