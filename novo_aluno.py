#!/usr/bin/env python3

from random import choice
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from login import login, ADMIN_ACCOUNT
from utils import random_string, wait_spinner, scroll_and_click, choose_from_select

def novo_aluno(driver, url = 'http://localhost:8000/vaspapp/aluno/add/'):
    # Generate values
    driver.get(url)

    today = date.today()

    # Start creation

    ## Fill fields
    driver.find_element_by_id('id_name').send_keys(random_string())
    driver.find_element_by_id('id_rg').send_keys(123456)
    driver.find_element_by_id('id_cpf').send_keys(89239469)
    driver.find_element_by_id('id_telefone').send_keys(991991991)
    select = Select(driver.find_element_by_name('id_curso'))
    select.select_by_index(1)

    ## Submit and wait
    scroll_and_click(driver, driver.find_element_by_id('submit-id-submit'))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'adicionar')))

if __name__ == '__main__':
    try:
        driver = webdriver.Chrome()

        login(driver, ADMIN_ACCOUNT)

        novo_aluno(driver)
    except e:
        print('Test number', i, 'has failed!!!')
    finally:
        driver.quit()
