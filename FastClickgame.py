#fast
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


#cookie clicker https://orteil.dashnet.org/cookieclicker/
#click test     https://clickspeedtest.com/5-seconds.html
path_to_extension = r'C:\Users\susan\Documents\1.34.0_22'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome("C:\chromedriver.exe", chrome_options=chrome_options)
driver.create_options()
driver.get("https://orteil.dashnet.org/cookieclicker/")
x=1
driver.implicitly_wait(5)

id = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(x,-1,-1)] #needs to be updated

def clickCookie():
    for i in range(100):
        id.click()

actions = ActionChains(driver)


for i in range(5000):
    clickCookie()
    count = int(cookie_count.text.split(" ")[0].replace(',', ''))
    for item in items:
        #print(items)
        try:
            value = int(item.text.replace(',', ''))
        except:
            value=count+1
        #print(value)
        if value <= count:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(item)
            upgrade_action.click()
            upgrade_action.perform()

    if i%20==0:
        try:
            x+=1
            items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(x,-1,-1)]
        except:
            pass
            #items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(x,-1,-1)]
        #print(x,items)
# time.sleep(1) # results are slow
# result = driver.find_element_by_css_selector('.times')
# print(f'Result: {result.text}\n')
# driver.close()
