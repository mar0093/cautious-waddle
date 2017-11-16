from selenium import webdriver
import time
import keyboard

def main():
    print('hello')
    nab_login()
    #buy("ddr.asx", str(2.00))
    sell("wbc.asx", str(32.83), str(10))

def nab_login():

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get('https://www.nabtrade.com.au/-/login/client-widget-login.html?provider...u/adfs/services/trust&returnurl=https://fss.nabtrade.com.au/auth/&')
    time.sleep(5)
    #browser.maximize_window()

    user = browser.find_element_by_css_selector('#usernameField')

    user.send_keys('13159242')
    password = browser.find_element_by_css_selector('#passwordField')
    password.send_keys('C@pital1')

    time.sleep(2)
    login = browser.find_element_by_css_selector('#loginlink')
    login.click()
    time.sleep(1)
    browser.get('https://nabtrade.com.au/trading/place-order')
    time.sleep(3)


def buy(share, price):
    quantity = str(400 // float(price)+ 1)
    keyboard.write(share)
    time.sleep(7)
    keyboard.press_and_release('tab')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(1)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    time.sleep(1)
    keyboard.write(quantity)
    time.sleep(1)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    time.sleep(1)
    keyboard.write(price)
    time.sleep(1)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    keyboard.write("a9YT")
    time.sleep(3)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    time.sleep(1)
    keyboard.press_and_release('enter')
    input("is it working?")



def sell(share, price, quantity):
    time.sleep(3)
    keyboard.write(share)
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    keyboard.press_and_release('tab')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(1)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('down')
    time.sleep(1)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    time.sleep(1)
    keyboard.write(quantity)
    time.sleep(1)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    time.sleep(1)
    keyboard.write(price)
    time.sleep(1)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    time.sleep(3)
    keyboard.press_and_release('enter')
    input("is it working?")


if __name__ == "__main__":
    main()

