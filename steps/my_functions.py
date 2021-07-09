import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
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
image_path = "C:/Users/RSB TRUCKING LLC/Desktop/wallet pic"

# url2 = "https://www.facebook.com/marketplace/you/selling"
title_verify = "//span[contains(text(),'wallet')]"

three_dots = "//div[@aria-label='More']//i "
delete_listing = "//span[contains(text(),'Delete Listing')]"
delete_button = "//div[@aria-label='Delete']"
yes_sold  = "//span[contains(text(),'Yes, sold on Facebook')]"
last_next_button = "//span[contains(text(),'Next')]"

# Scenario 1
def login_to_facebook():
    """Launching Facebook Marketplace and logging in with my email and password """
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

# Scenario 2
def create_new_listings():
    """Creating new listing in Facebook Marketplace"""

    element = driver.find_element_by_xpath(create_new_listing)
    print("clicking the element")
    element.click()
    time.sleep(1)

    element = driver.find_element_by_xpath(item_for_sale)
    print("clicking the element")
    element.click()
    time.sleep(1)

    image_upload = driver.find_element_by_xpath(upload_xpath)
    image_upload.send_keys(image_path)

    element = driver.find_element_by_xpath(title_input)
    print(f"entering the following text : wallet")
    element.clear()
    element.send_keys('wallet')
    time.sleep(1)

    element = driver.find_element_by_xpath(price_input)
    print(f"entering the following text : 15")
    element.clear()
    element.send_keys('15')
    time.sleep(1)

    element = driver.find_element_by_xpath(category_list)
    print("clicking the element")
    element.click()
    time.sleep(1)

    element = driver.find_element_by_xpath(category_item)
    print("clicking the element")
    element.click()
    time.sleep(1)

    element = driver.find_element_by_xpath(category_sub_item)
    print("clicking the element")
    element.click()
    time.sleep(1)

    element = driver.find_element_by_xpath(condition_list)
    print("clicking the element")
    element.click()
    time.sleep(1)

    element = driver.find_element_by_xpath(condition_option)
    print("clicking the element")
    element.click()
    time.sleep(1)

    element = driver.find_element_by_xpath(description)
    print(f"entering the following text : Hello World")
    element.clear()
    element.send_keys('Hello World')
    time.sleep(1)

    element = driver.find_element_by_xpath(product_tags)
    print(f"entering the following text : leather wallet")
    element.clear()
    element.send_keys('leather wallet')
    time.sleep(1)

    element = driver.find_element_by_xpath(sku_numbers)
    print(f"entering the following text : 123456")
    element.clear()
    element.send_keys('123456')
    time.sleep(1)

    element = driver.find_element_by_xpath(location)
    print(f"entering the following text : Las Vegas")
    element.clear()
    element.send_keys('Las Vegas')
    time.sleep(1)

    next_button = driver.find_element_by_xpath(next_button_xpath)
    if next_button.is_enabled():
        next_button.click()
        print("Next button is clicked.")

    element = driver.find_element_by_xpath(publish_button)
    print("clicking the element")
    element.click()
    time.sleep(1)

    url2 = driver.current_url
    print(url2)
    assert url2 == "https://www.facebook.com/marketplace/you/selling"

    active_item1 = driver.find_element_by_xpath(title_verify)
    time.sleep(5)
    assert active_item1.is_displayed()
    print("Test is successfully executed!!")


# Scenario 3
def listing_removal():
    """deleting listed item on Facebook Marketplace"""
    element = driver.find_element_by_xpath(three_dots)
    print("clicking the element")
    element.click()
    time.sleep(1)

    element = driver.find_element_by_xpath(delete_listing)
    print("clicking the element")
    element.click()
    time.sleep(1)

    element = driver.find_element_by_xpath(delete_button)
    print("clicking the element")
    element.click()
    time.sleep(1)

    element = driver.find_element_by_xpath(yes_sold)
    print("clicking the element")
    element.click()
    time.sleep(1)

    element = driver.find_element_by_xpath(last_next_button)
    print("clicking the element")
    element.click()
    time.sleep(1)

    active_item1 = driver.find_element_by_xpath(title_verify)
    assert not active_item1.is_displayed()














