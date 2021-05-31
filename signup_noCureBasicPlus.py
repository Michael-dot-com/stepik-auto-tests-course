from selenium import webdriver
import time 

link = "https://lb-test7.lokalebasen.dk/signup"

try:
        browser = webdriver.Chrome()
        browser.get(link)

        option1 = browser.find_element_by_css_selector(".cookie-consent-confirm-box")
        option1.click()
        browser.execute_script("window.scrollBy(0, 500);")
        input1 = browser.find_element_by_css_selector("[id='company_name']")
        input1.send_keys("Michael and Co")
        input2 = browser.find_element_by_css_selector("[id='vat_id']")
        input2.send_keys("1234567890123")
        input3 = browser.find_element_by_css_selector("[id='name']")
        input3.send_keys("Michael")
        input4 = browser.find_element_by_css_selector("[id='email']")
        input4.send_keys("noCureBasicPlus@noCureBasicPlus.com")
        input5 = browser.find_element_by_css_selector("[id='phone_number']")
        input5.send_keys("12312312")
        input6 = browser.find_element_by_css_selector("[id='password']")
        input6.send_keys("qwerty")
        option2 = browser.find_element_by_css_selector("[id='noCureBasicPlus']")
        option2.click()
        input7 = browser.find_element_by_css_selector(".sign-up-form__terms-conditions-label div")
        input7.click()
        button = browser.find_element_by_xpath('//button[text()="Opret konto og kom i gang"]')
        button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
