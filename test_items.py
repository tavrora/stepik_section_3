import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_exists_button_add_basket(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button.get_attribute('type') == 'submit'

    # запасной вариант
    # try:
	# 	browser.find_element_by_css_selector(".btn-add-to-basket")
	# except NoSuchElementException:
	# 	return False
	# return True
