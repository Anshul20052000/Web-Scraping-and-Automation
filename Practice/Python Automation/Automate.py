from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(0)
driver.get("https://www.google.co.in/")
time.sleep(0)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div').click()
driver.find_element_by_name('q').send_keys('Youtube')
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div/div[1]/a/h3').click()
driver.find_element_by_name('search_query').send_keys('Marvel Eternals')
time.sleep(1)
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div').click()
driver.find_element_by_xpath('//*[@id="movie_player"]/div[1]').send_keys("f")

