from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



@then('Verify search results has {expected_search}')
def verify_search_results(self, expected_search):
    self.app.search_results_page.verify_search_results(expected_search)



# Verify URL
# @then('Verify that URL has {expected_url}')
# def verify_url_page(self, expected_url):
#     self.app.search_results_page.verify_partial_url(expected_url)