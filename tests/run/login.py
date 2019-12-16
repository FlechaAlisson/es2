#!/usr/bin/env python3

from collections import namedtuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSelenium1():

    def test_login(driver = webdriver.Chrome(), url='http://localhost:8000/accounts/login/'):
        driver.get(url)

        driver.find_element_by_id('id_username').send_keys('andrelopes')
        driver.find_element_by_id('id_password').send_keys('80cc1200')

        driver.find_element_by_id('submit').click()
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'adicionar')))
        driver.quit()
        print("Login SUCCESS!\n")


    # if __name__ == '__main__':
    #     try:
    #         driver = webdriver.Chrome()

    #         login(driver, ADMIN_ACCOUNT)
    #     finally:
    #         driver.quit()
