#!/usr/bin/env python3

from random import choice
from datetime import date
from random import randrange

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from login import TestSelenium1
from utils import random_string, wait_spinner, scroll_and_click, choose_from_select


class TestSelenium2():

    def test_nota(self, url = 'http://localhost:8000/vaspapp/nota/add/'):
        # Generate values
        driver = webdriver.Chrome()

        driver.get('http://localhost:8000/accounts/login/')

        driver.find_element_by_id('id_username').send_keys('andrelopes')
        driver.find_element_by_id('id_password').send_keys('80cc1200')

        driver.find_element_by_id('submit').click()
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'adicionar')))
        print("Login SUCCESS!\n")

        driver.get(url)

        # Start creation

        ## Fill fields
        select = Select(driver.find_element_by_id('id_matricula'))
        select.select_by_index(1)
        driver.find_element_by_id('id_data').send_keys('16/12/2019')
        driver.find_element_by_id('id_nota').send_keys(randrange(11))
        

        ## Submit and wait
        scroll_and_click(driver, driver.find_element_by_id('submit-id-submit'))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'adicionar')))
        driver.quit()
        print("Nota SUCCESS!\n")
