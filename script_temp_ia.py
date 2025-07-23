from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Configurando o serviço do driver do Chromium
service = Service('driver\chromedriver.exe')  # Insira o caminho para o chromedriver

# Inicializando o driver do Chromium
driver = webdriver.Chrome(service=service)

try:
    # Acessar o aplicativo da plataforma AcordeLab
    driver.get("https://almsantana.github.io/")

    time.sleep(3)  # Aguardar 3 segundos

    # Preencher o campo "E-mail" com um e-mail válido
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("email@acordelab.com.br")

    # Preencher o campo "Senha" com uma senha válida
    password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
    password_input.send_keys("123senha")

    # Clicar no botão "Entrar"
    enter_button = driver.find_element(By.CLASS_NAME, "botao-login")
    enter_button.click()

    time.sleep(3)  # Aguardar 3 segundos

finally:
    # Fechar o navegador após a execução do teste
    driver.quit()