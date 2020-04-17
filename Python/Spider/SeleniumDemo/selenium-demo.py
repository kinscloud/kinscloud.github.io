from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver_path = "chrome的完整路径"
# driver = webdriver.Chrome(executable_path=driver_path)
# options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server=http://49.70.32.224:9999")
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
submitTag = driver.find_element_by_id('su')
print(submitTag.get_attribute('value'))
driver.save_screenshot('baidu.png')
# driver.execute_script("window.open('https://www.douban.com')")
#driver不随可视窗口切换，需要在代码中切换，否则获取代码和元素将不成功
# driver.switch_to_window(driver.window_handles[1])
# print(driver.current_url)

#driver.implicitly_wait(5)

# element = WebDriverWait(driver,10).until(
#     EC.presence_of_element_located((By.ID,'kw'))
# )

# inputTag = driver.find_element_by_id('kw')
# submitTag = driver.find_element_by_id('su')

# actions = ActionChains(driver)
# actions.move_to_element(inputTag)
# actions.send_keys_to_element(inputTag,'python')
# actions.move_to_element(submitTag)
# actions.click(submitTag)
# actions.perform()
time.sleep(10)