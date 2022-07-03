#importar os arquivos Web
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#importar funções tempo
import time
#importar função item randomico
import random
#importar login e senha
from login import credenciais
#importar comentarios
from comentario import listacomentario
comentariorandomico = random.choice(listacomentario)
#criar itens
links_tratados =[]
#Tecla tab
import pyautogui

#abrir navegador
driver = webdriver.Chrome()
url = "https://www.instagram.com/"
drpatricia ="https://www.instagram.com/dra.patriciadominico/"

def inicio(url):
    print("Abrindo o navegador...")
    driver.get(url)
    time.sleep(1)
    autenticar()
    print("Navegador fechado")


def autenticar():
    imputs_login = driver.find_elements(By.CLASS_NAME,"_2hvTZ")
    #escrever login
    imputs_login[0].click()
    imputs_login[0].send_keys(credenciais[0])
    # escrever senha
    imputs_login[1].click()
    time.sleep(0.5)
    imputs_login[1].send_keys(credenciais[1])
    time.sleep(2)
    entrar = '//*[@id="loginForm"]/div/div[3]/button/div'
    #clicar em entrar
    driver.find_element(by=By.XPATH,value = entrar).click()
    time.sleep(5)
    pyautogui.press("tab")
    time.sleep(0.1)
    pyautogui.press("tab")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.1)

    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(0.1)
    pyautogui.press("tab")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(3)
    redirecionar()

def redirecionar():
    print('----------------redirecionar---------------------------------')
    driver.get(drpatricia)
    time.sleep(3)
    #descer pagina do feed
    descer = 0
    while descer < 5:
        descer = descer +1
        #pega o elemento html
        html = driver.find_element_by_tag_name("html")
        #abaixa a tela
        html.send_keys(Keys.END)
        time.sleep(3)
    pegar_POSTS()

def pegar_POSTS():
    #localiza o elemento "a"
    posts = driver.find_elements(By.TAG_NAME,'a')
    for post in posts:
        #pega os links
        post_link =post.get_attribute("href")
        
        #se tiver a letra "p" de postagem adicona a lista 
        if"/p/" in post_link:
                links_tratados.append(post_link)
            
        else:
            print("fora do padrao")
    print("LINKS TRATADOS")
    print(links_tratados)
    time.sleep(3)
    abrirLinks(links_tratados)

def abrirLinks(lista):
    for item in lista:
        driver.get(item)               
        time.sleep(5)
        curtir()
        time.sleep(5)
  
def curtir():
    print("-----------------------------------------Curtir------------------------------------------------")
    time.sleep(2)
    #Dando certo o curtir
    driver.find_element(by=By.CLASS_NAME, value='_aamw').click()
    comentar()



def comentar():
    listacomentario=["top", "bom de mais", "adoro", "#ficadica ;)"]
    print('-------------------------------------------Comentar--------------------------------------------')
    #escrever login
    driver.find_element(by=By.TAG_NAME, value='textarea').click()
    time.sleep(3)
    driver.find_element(by=By.TAG_NAME, value='textarea').send_keys(comentariorandomico)
    time.sleep(3)
    pyautogui.press("enter")
    print("-------------------------------------deu certo----------------------------------------------------------")
inicio(url)