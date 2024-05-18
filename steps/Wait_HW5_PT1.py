from time import sleep

from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# @given('Open Target page HW_5')
# def open_target(context):
#     context.driver.get('https://www.target.com/')
#     sleep(5)


@when("Verify target circle HW_5")
def input_search(context):
    context.driver.find_element(By.XPATH, value="//a[@id='utilityNav-circle']").click()
    links = context.driver.find_elements(By.XPATH, value="//div[@class='cell-item-content']")
    print(len(links))
    assert len(links) == 10, f"Expected 10 links, but got {len(links)}"
    sleep(5)


@when("Search for item {search_text} HW_5")
def input_search(context, search_text):
    # Find the search input field and send keys
    search_input = context.driver.find_element(By.ID, 'search')
    search_input.send_keys(search_text)

    # Find and click the search button
    search_button = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-test='@web/Search/SearchButton']"))
    )
    search_button.click()

@when("Click on add to cart HW_5")
def target_add_to_cart(context):
    # Wait for 5 seconds
    WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[@id='addToCartButtonOrTextIdFor16849682']")))
    # Find and click the element
    context.driver.find_element(By.XPATH, value="//button[@id='addToCartButtonOrTextIdFor16849682']").click()

    # Wait for 3 seconds
    WebDriverWait(context.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//button[@data-test='fulfillment-cell-shipping']")))
    # Find and click the element
    context.driver.find_element(By.XPATH, value="//button[@data-test='fulfillment-cell-shipping']").click()

    # Wait for 3 seconds
    WebDriverWait(context.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//button[@data-test='shippingButton']")))
    # Find and click the element
    context.driver.find_element(By.XPATH, value="//button[@data-test='shippingButton']").click()

    # Wait for 3 seconds
    WebDriverWait(context.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'View cart')]")))
    # Find and click the element
    context.driver.find_element(By.XPATH, value="//a[contains(text(),'View cart')]").click()

@then('Verify item in cart HW_5')
def item_in_cart(context):
    actual_text = context.driver.find_element(By.XPATH, value="//div[contains(text(),'Lavazza Classico Medium Roast Ground Coffee - 12oz')]")
    assert 'Lavazza Classico Medium Roast Ground Coffee - 12oz' in actual_text.text, f'{actual_text} is NOT in cart'
    print("Test case has passed")



