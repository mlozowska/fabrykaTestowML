"""
identify and navigate to elements
scroll down the page to the specific element
capture and save a screenshot
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://fabrykatestow.pl/')

# go to KURSY tab
element = driver.find_element_by_id("menu-item-622")
element.click()

# go to STRONA KURSU tab
strona_kursu = driver.find_element_by_class_name('elementor-button-text')
strona_kursu.click()

## scroll down to the photo of the instructor
driver.execute_script('window.scrollTo(0,1700)')

# take a screenshot and store in the given location
driver.save_screenshot("C:/Users/Administrator/PycharmProjects/taps_git/homework/screenshot/photo.png")

driver.close()
driver.quit()
