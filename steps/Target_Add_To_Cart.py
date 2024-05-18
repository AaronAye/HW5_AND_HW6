from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By



# @when("Verify target circle HW")
# def input_search(context):
#     context.driver.find_element(By.XPATH, value="//a[@id='utilityNav-circle']").click()
#     links = context.driver.find_elements(By.XPATH, value="//div[@class='cell-item-content']")
#     print(len(links))
#     assert len(links) == 10, f"Expected 10 links, but got {len(links)}"
#     sleep(5)


# @when("Search for {search_text} HW")
# def input_search(context, search_text):
#     context.driver.find_element(By.ID,'search').send_keys(search_text)
#     context.driver.find_element(By.XPATH, value="//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(5)

@when("Click add to cart icon")
def add_to_cart(self):
    self.app.cart_page.add_to_cart()

    # sleep(5)
    # context.driver.find_element(By.XPATH, value="//button[@id='addToCartButtonOrTextIdFor16849682']").click()
    # sleep(3)
    # context.driver.find_element(By.XPATH, value="//button[@data-test='fulfillment-cell-shipping']").click()
    # sleep(3)
    # context.driver.find_element(By.XPATH, value="//button[@data-test='shippingButton']").click()
    # sleep(3)
    # context.driver.find_element(By.XPATH, value="//a[contains(text(),'View cart')]").click()


@then('Verify item in cart')
def verify_cart(self):
    self.app.cart_page.verify_cart(self)

# def item_in_cart(context):
#     actual_text = context.driver.find_element(By.XPATH, value="//div[contains(text(),'Lavazza Classico Medium Roast Ground Coffee - 12oz')]")
#     assert 'Lavazza Classico Medium Roast Ground Coffee - 12oz' in actual_text.text, f'{actual_text} is NOT in cart'
#     print("Test case has passed")



