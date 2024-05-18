from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

CART_ICON = (By.XPATH, "//div[@data-test='@web/CartIcon']")
EMPTY_CART_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")
@given('Open Target page test')
def open_target(context):
    context.wait.until(EC.url_contains(context.driver.get('https://www.target.com/')))

@when('Click on cart icon test')
def click_cart_icon(context):
    context.wait.until(EC.element_to_be_clickable(context.driver.find_element(*CART_ICON).click()))


@then('Verify empty cart message test')
def empty_cart_text(context):
    context.wait.until(EC.text_to_be_present_in_element(EMPTY_CART_MSG))
    actual_text = context.driver.find_element(*EMPTY_CART_MSG)
    assert 'Your cart is empty' in actual_text.text, f'Your cart is empty is not in {actual_text}'
    print("Test case has passed")



