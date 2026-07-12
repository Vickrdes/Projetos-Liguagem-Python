#bibliotecas 
import pyautogui
import time
pyautogui.PAUSE = 1
# Passo 1 - entrar no sistema da empresa
#abrir o navegador 
pyautogui.press("win")
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(5)

# Passo 2 - fazer login
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#fazer uma pausa maior para o site carregar 
time.sleep(3) #espera 3 segundos 

 #clicar e escrever o e-mail
pyautogui.click(x=739, y=372)
pyautogui.write('vitoria.souza@gmail.com')

#clicar e escrever a senha 
pyautogui.press('tab') #passa para o proximo campo
pyautogui.write('123456789987654321')

#clicar no logar
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(4)



# Passo 3 - abrir a base de dados
import pandas as pd

tabela = pd.read_csv('produtos.csv')#le o arquivo, pode passar ou o caminho ou o nome se estiver na pasta do cod
print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=718, y=259)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim

    

