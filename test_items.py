import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_available_in_page(browser):
    browser.get(link)
    time.sleep(10)
    button=browser.find_element_by_css_selector("button.btn")
    assert button is not None, "Button not found"