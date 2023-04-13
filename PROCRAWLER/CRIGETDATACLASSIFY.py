from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
import time


# open chromium
driver = webdriver.Chrome()
driver.get("https://fnet.bmfbovespa.com.br/fnet/publico/pesquisarGerenciadorDocumentosCertificadosCVM?paginaCertificados=true&tipoFundo=&administrador=&idCategoriaDocumento=0&idTipoDocumento=0&idEspecieDocumento=0&situacao=&cnpj=&dataReferencia=&dataInicial=01%2F10%2F2019&dataFinal=29%2F10%2F2019&idModalidade=&palavraChave=")

open_modal = driver.find_element(By.ID, "showFiltros")
open_modal.click()

time.sleep(1)
comunicated_class = driver.find_element(By.ID, "s2id_autogen1")
comunicated_class.send_keys(Keys.ENTER)

CRI = driver.find_elements(By.CLASS_NAME, "select2-results-dept-0.select2-result.select2-result-selectable")[1]
time.sleep(1)
CRI.click()

category = driver.find_element(By.ID, "s2id_autogen2")
category.send_keys(Keys.ENTER)

INFORME = driver.find_element(By.ID, "select2-result-label-39")
INFORME.click()

data_inf = driver.find_element(By.ID, "dataFinal")
data_inf.clear()

filterBtn = driver.find_element(By.ID, 'filtrar')
filterBtn.click()

#raspagem
time.sleep(3)
pagina_atual = driver.page_source
soup = BeautifulSoup(pagina_atual, 'html.parser')
    
    
max_screen_exibition = driver.find_element(By.NAME, 'tblDocumentosEnviados_length').find_elements(By.TAG_NAME, 'option')[-1]
max_screen_exibition.click()
time.sleep(1)
pagesQt = soup.find_all('a')
pagesQt = int(int(pagesQt[-2].text) / 9.9)
classes = []
codsifs = []
isins = []


for i in range(0, pagesQt, 1):
    IDS = []

    time.sleep(3)
    pagina_atual = driver.page_source
    soup = BeautifulSoup(pagina_atual, 'html.parser')
    infos = soup.find_all('tr')
    for all_infos in infos:
        try:
            info = all_infos.find_all('td')
            doc_view = all_infos.find_all('a')
            if info[2].text == 'Informe Mensal de CRI':
                try:
                    id = str(doc_view[0])[32:]
                    id = id[:id.find("&")]
                    IDS.append(id)
                except:
                    pass
        except:
            pass


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
        try:
            tr = soup.find_all('table')[2].find_all('tr')
        except:
            try:
                tr = soup.find_all('table')[2].find_all('tr')
            except:
                print(id_do_comunicado)
        for i in tr:
            if not i.has_attr('class') or 'gray' not in i['class']:
                linha = i.find_all('td')
                classe = linha[0].text
                cod_if = linha[3].text
                isin = linha[4].text
                classes.append(classe)
                codsifs.append(cod_if)
                isins.append(isin)
            



    driver.find_element(By.ID, 'tblDocumentosEnviados_next').click()