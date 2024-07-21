from playwright.sync_api import Page
from time import sleep
from pandas import DataFrame


def setlistinfo(db:DataFrame):
    values:list [str] = []
    for value in db.values:
        values.append(str(value))
    return values

def fillForms(page:Page, sex:str, url:str):
    page.locator(selector='//*[@id="i5"]/div[3]/div').check()
    page.get_by_label(f'{sex}').check()
    page.locator(selector='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').fill('Centro')
    page.get_by_label('25 a 34' ).check()
    page.get_by_label('Ensino superior').check()
    page.locator('//*[@id="i82"]/div[3]/div').check()
    page.get_by_label('Leo Geisteosa').check()
    page.locator('//*[@id="i119"]/div[3]/div').check()
    page.get_by_label('Ruim').check()
    page.locator('//*[@id="i151"]/div[3]/div').check()
    page.locator('//*[@id="i167"]/div[3]/div').check()
    page.locator('//*[@id="i180"]/div[3]/div').check()
    page.locator('//*[@id="i190"]/div[3]/div').check()
    page.locator('//*[@id="i203"]/div[3]/div').check()
    sleep(1)
    page.locator(selector='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    sleep(2)
    page.goto(url)
    sleep(1)
    page.goto(url)

    
