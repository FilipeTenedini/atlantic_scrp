from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
import time


# open chromium
driver = webdriver.Chrome()
driver.get('https://fnet.bmfbovespa.com.br/fnet/publico/pesquisarGerenciadorDocumentosCertificadosCVM?paginaCertificados=true&tipoFundo=&administrador=&idCategoriaDocumento=0&idTipoDocumento=0&idEspecieDocumento=0&situacao=&cnpj=&dataReferencia=&dataInicial=01%2F10%2F2019&dataFinal=29%2F10%2F2019&idModalidade=&palavraChave=')


