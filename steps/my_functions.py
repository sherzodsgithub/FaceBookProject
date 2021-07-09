import time
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

create_new_listing = "//span[contains(text(),'Create New Listing')]"
item_for_sale = "//span[contains(text(),'Item for Sale')]"

upload_xpath = "//input[@type='file' and contains(@accept, 'image')]"
title_input = "//label[@aria-label='Title']//input[contains(@id, 'jsc_c_')]"
price_input = "//label[@aria-label='Price']//input[contains(@id, 'jsc_c_')]"
category_list = "//label[@aria-label='Category']//span"
category_item = "//span[contains(text(),'Electronics')]"
category_sub_item = "//span[contains(text(),'Blank Media')]"
condition_list = "//span[contains(text(),'Condition')]"
condition_option = "//div[contains(text(),'New')]"
description = "//label[@aria-label='Description']//textarea"
product_tags = "//label[@aria-label='Product tags']//textarea"
sku_numbers = "//label[@aria-label='SKU']//input"
location = "//label[@aria-label='Location']//input"
next_button_xpath = "//div[@aria-label='Next']"
publish_button = "//span[contains(text(),'Publish')]"


url2 = "https://www.facebook.com/marketplace/you/selling"
title_verify = "//span[contains(text(),'wallet')]"


three_dots = "//div[@aria-label='More']//i "
delete_listing = "//span[contains(text(),'Delete Listing')]"
delete_button = "//div[@aria-label='Delete']"


#Scenario 1
def login_to_facebook():

    driver.get(url)
    print(f"opened the browser and website :{url}")
    time.sleep(1)


    element = driver.find_element_by_xpath(email_input)
    print(f"entering the following text : {email}")
    element.clear()
    element.send_keys(email)
    time.sleep(1)

    element = driver.find_element_by_xpath(password_input)
    print(f"entering the following text : {password}")
    element.clear()
    element.send_keys(password)
    time.sleep(1)

    element = driver.find_element_by_xpath(login_button)
    print("clicking the element")
    element.click()
    time.sleep(1)
