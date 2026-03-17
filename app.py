import openpyxl #importação 
from urllib.parse import quote
import webbrowser #para abrir o navegador. 
import time
import pyautogui
from PIL import Image

#abre o navegador
webbrowser.open('https://web.whatsapp.com/')
time.sleep(10)

#Abre arquivo
planilha = openpyxl.load_workbook('lista_candidatos.xlsx')

#Seleciona pasta do arquvio 
paginas = planilha['Planilha1']

#Cria laço de repetição para entrar em contato
for linha in paginas.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value #o padrão precisa ser codigo do pais + codigo de area + numero de telefone 
    cargo = linha[2].value 

    # aqui vai ser o link do telefone do wpp"
    mensagem_personalisada = (f"Olá, {nome}, nós da Atena Rh parabenizamos pela contratação para o cargo {cargo}."
                              "Poderia nos confirmar se já está trabalhando com a empresa?")
    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem_personalisada)}'

    #Envia a mensagem e em seguida fecha 
    webbrowser.open(link_mensagem_whatsapp)
    time.sleep(30)
    try:
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.hotkey('ctrl','w')
        time.sleep(5)
    
    except:
        print(f'Não foi possivel enviar mensagem para {nome}')
        with open('erros.csv','a',newline='',encoding='utf-8') as arquivo:
            arquivo.write(f'Não foi possivel contatar o candidato: {nome}, telefone: {telefone}')
    
