from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Runs the code
def main():
    """Creates a ChromeDriver, maximises, opens the AM live site then asserts whether the correct page has been
    called """
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://configurator.astonmartin.com/#/')
    wait = WebDriverWait(browser, 15)
    assert "astonmartin" in browser.current_url, "URL not correct."

    # intro = "button[ng-click='configurator.toggleIntro()']"
    intro = "button.am-360-toggle-btn"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, intro)))
    browser.find_element_by_css_selector(intro).click()
    # browser.find_element_by_css_selector("button[ng-click='configurator.toggleIntro()']").click()

    """Closes the 'View Policy' frame"""
    policy = "button[ng-click='closePolicy()']"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, policy)))
    browser.find_element_by_css_selector(policy).click()

    """Finds current country selected """
    currentCountry = browser.find_element_by_css_selector('p.overlay-item-active').text
    print("This is the country selected: " + currentCountry)
    # assert (currentCountry == 'United States'), ("Current Selection: " + currentCountry)

    print(selectCountry(browser, "United Kingdom"))

    print(selectLanguage(browser, "English"))
    # browser.quit()


# Method to select a country by first asserting the country isn't already selected,
# followed by iterating through all countries to match the parameter.
def selectCountry(driver, country):
    p = driver.find_element_by_css_selector("p[ng-click='updateRegion(countryCode)']")
    assert (p.text != country), (country + "is already selected!")

    list_of_countries = []
    cText = driver.find_elements_by_css_selector("p[ng-click='updateRegion(countryCode)']")
    for i in cText:
        list_of_countries.append(i.text)
    pprint("These are the country options: " + '\n' + list_of_countries.__str__())

    assert country in list_of_countries, "This country isn't in the list!"

    for c in cText:
        if c.text in list_of_countries:
            if c.text == country:
                c.click()
    return "The country {} is now selected.".format(driver.find_element_by_css_selector('p.overlay-item-active').text)


def selectLanguage(driver, lang):
    p = driver.find_element_by_css_selector("p[ng-click='updateLanguage(language.code)']")
    assert (p.text != lang), (lang + "is already selected!")


if __name__ == "__main__":
    main()
