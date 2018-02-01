from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://configurator.astonmartin.com/#/')

    wait = WebDriverWait(browser, 15)
    assert "astonmartin" in browser.current_url

    """Closes the 'View Policy' frame"""
    policy = "button[ng-click='closePolicy()']"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, policy)))
    browser.find_element_by_css_selector(policy).click()

    """Finds current country selected """
    # currentCountry = browser.find_element_by_css_selector('p.overlay-item-active').text
    #  print("This is the country selected: " + currentCountry)
    # assert (currentCountry == 'United States'), ("Current Selection: " + currentCountry)

    print(selectCountry(browser, "United Kingdom"))
    currentCountry = browser.find_element_by_css_selector('p.overlay-item-active').text
    print("You have changed the country to : " + currentCountry)
    WebDriverWait(browser, 150)
    # browser.quit()


def selectCountry(driver, country):
    p = driver.find_element_by_css_selector('p.overlay-item-active')
    assert (p.text != country), (country + "is already selected!")

    list_of_countries = []
    cText = driver.find_elements_by_css_selector("p[ng-click='updateRegion(countryCode)']")
    for i in cText:
        list_of_countries.append(i.text)
    # return list_of_countries
    print(list_of_countries)

    assert country in list_of_countries, "This country isn't in the list!"

    for c in cText:
        if c.text in list_of_countries:
            if c.text == country:
                c.click()
    test = c.text + " has been selected"

    print(test)


if __name__ == "__main__":
    main()
