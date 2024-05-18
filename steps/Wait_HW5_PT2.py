from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


def open_target_url(context):
    context.driver.get('https://www.target.com/p/A-91511634?preselect=91511683')

# List of CSS selectors
COLOR_LOOP = [
    "button[aria-label='dark khaki']",
    "button[aria-label='black/gum']",
    "button[aria-label='stone/grey']",
    "button[aria-label='white/gum selected']"
]

def loop_through_colors(context):

    for color in COLOR_LOOP:

    # Wait for the element to be clickable

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, color))
    )
    # Click on the element
    element.click()

    # Wait for the element to be in the selected state
    selected_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f"{color}[aria-selected='true']"))
    )

    # Verify the element is selected
    assert selected_element, f"Color not selected: {color}"

    # Wait for 2 seconds before moving to the next color
    driver.implicitly_wait(2)

# Close the driver
driver.quit()