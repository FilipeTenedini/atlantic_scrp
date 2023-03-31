import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument("--headless")
from bs4 import BeautifulSoup
driver = webdriver.Chrome(chrome_options=options)
from _db import IDS

classes = []
codsifs = []
isins = []

for id_do_comunicado in IDS:
    # Navegar para a página principal
    driver.get(f"https://fnet.bmfbovespa.com.br/fnet/publico/visualizarDocumento?id={id_do_comunicado}&cvm=true/")

    # Localizar o elemento <iframe>
    iframe = driver.find_element(By.TAG_NAME, "iframe")

    # Mudar para o contexto do iframe
    driver.switch_to.frame(iframe)

    # Extrair o conteúdo do elemento <body>
    body = driver.find_element(By.TAG_NAME, "body")
    html = body.get_attribute("outerHTML")
    soup = BeautifulSoup(html, "html.parser")
    tr = soup.find_all('table')[2].find_all('tr')
    for i in tr:
        if not i.has_attr('class') or 'gray' not in i['class']:
            linha = i.find_all('td')
            classe = linha[0].text
            cod_if = linha[3].text
            isin = linha[4].text
            classes.append(classe)
            codsifs.append(cod_if)
            isins.append(isin)

df = pd.DataFrame({'classes': classes, 'ifs': codsifs, "isin": isins})
df.to_excel('CRA_INFOS.xlsx')