from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
# driver.set_page_load_timeout(15)
# driver.implicitly_wait(15)
driver.get("https://www.suning.com")
try:
    input = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'searchKeywords'))
    )
    print(input)
    # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # print(driver.page_source)
except TimeoutException:
    print('Time out')
finally:
    driver.quit()
