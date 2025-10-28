import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Link feature file 
scenarios('../features/example.feature')

@given("I start the browser")
def start_browser(browser):
    pass #browser started in fixture

@when(parsers.parse('I navigate to "{url}"'))
def navigate(browser, url):
    browser.get(url)

@when(parsers.parse('I click on the "{link_text}" link'))
def click_link(browser, link_text):
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, link_text))).click()

@then(parsers.parse('A link with text "{link_text}" must be present'))
def check_link_text_present(browser, link_text):
    elements = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, link_text)))
    
    #Verification of link text
    found = False
    for i in elements:
        if i.text.strip() == link_text:
            found = True
            break

    assert found, f"Link text '{link_text}' not found on page"

@then(parsers.parse("the 'Domain Names' box must contain \"{new_text}\" at index {index:d}"))
def check_domain_names_value(browser, new_text, index):
    domain_links = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#nav_dom_top li a")))
    #Verification 1
    assert len(domain_links) > index, f"Expected at least {index +1 } links under 'Domain Names' but there are not enough links"
    
    #Extract text at given index from domain_links
    actual_text = domain_links[index].text.strip()

    #Verification 2
    assert actual_text == new_text, f'Expected "{new_text}" at index {index}, but found "{actual_text}".'


