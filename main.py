from playwright.sync_api import sync_playwright
import pandas as pd
from time import sleep
import service.functions as service

db = pd.read_excel('DB_POLICT.xlsx')

# print(db)
# print(db["sexo"])

print(db)



list_of_type: list[str] = service.setlistinfo(db=db["sexo"])
voto = 0
number_votos = 0
URL_FORMS = ""


number_votos = int(input("Quantos Votos Deseja Efetuar ?"))

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False,timeout=50000)
    page = browser.new_page()
    page.goto(URL_FORMS)
    
        
    for person in list_of_type:
        sleep(2)
        if voto < number_votos:
            service.fillForms(page=page,sex=f"{person}",url=URL_FORMS)
            voto = voto + 1
        else:
            break
        print(f"Vota da pessoa numero Nº -> {voto}")

print('O votosForam efetuados com sucesso...')
print('Pesquisa finalizada')
