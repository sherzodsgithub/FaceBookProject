from selenium import webdriver

driver = webdriver.Chrome()
# driver.maximize_window()
driver.implicitly_wait(20)

import yaml
from os.path import dirname, abspath

ROOT_DIR = dirname(dirname(abspath(__file__)))
def load_yaml(filepath):
    with open(filepath, 'r') as data:
        document = yaml.safe_load(data)
    return document


data = load_yaml(f"{ROOT_DIR}/data/config.yml")

url = data['url']
email = data['email']
password = data['password']

email_input = "//input[@name='email']"
password_input = "//input[@name='pass']"
login_button = "//div[@aria-label='Accessible login button']"


upload_xpath = "//input[@type='file' and contains(@accept, 'image')]"
price_input = "//label[@aria-label='Price']//input[contains(@id, 'jsc_c_')]"
title_input = "//label[@aria-label='Title']//input[contains(@id, 'jsc_c_')]"
category_list = "//label[@aria-label='Category']//span"
category_item = "//span[contains(text(),'Electronics')]"
category_sub_item = "//span[contains(text(),'Blank Media')]"
condition_list = "//span[contains(text(),'Condition')]"
condition_option = "//div[contains(text(),'Used - Like New')]"
next_button_xpath = "//div[@aria-label='Next']"