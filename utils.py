from time import sleep
from random import choice
from string import ascii_letters, digits


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


alphanumeric = ascii_letters + digits


def random_string(length=10):
    return choice(ascii_letters) + ''.join(choice(alphanumeric) for i in range(length-1))


def wait_spinner(driver):
    sleep(0.11) # Enough time for the spinner to show up.
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, 'spinner')))


def scroll_and_click(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).click(element).perform()


def choose_from_select(driver, select_id, select_option_id):
    scroll_and_click(driver, driver.find_element_by_id(select_id))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'menu-')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, select_option_id)))
    scroll_and_click(driver, driver.find_element_by_id(select_option_id))
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, 'menu-')))
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, select_option_id)))