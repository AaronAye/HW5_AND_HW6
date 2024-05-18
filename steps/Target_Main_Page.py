from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By


@given("Open Target main page")
def open_target(context):
   # context.driver.get('https://www.target.com/')
   context.app.main_page.open_main()



@when("Search for {search_text}")
def input_search(context, search_text):
    #context.driver.find_element(By.ID,'search').send_keys(search_text)
    #context.driver.find_element(By.XPATH, value="//button[@data-test='@web/Search/SearchButton']").click()
    context.app.header.search_products(search_text)
    sleep(5)


@when("Click on Cart icon")
def target_search(context):
    context.driver.find_element(By.XPATH, value="//div[@data-test='@web/CartIcon']").click()

