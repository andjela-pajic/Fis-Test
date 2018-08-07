import os
import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

username = 'pile2707'
email = 'andjela.pajic90@gmail.com'

try:
    driver = webdriver.Chrome()
    driver.get("https://www.fisglobal.com/")
    element_to_hover_over = driver.find_element_by_xpath('//*[@id="navbar-collapse-grid"]/ul[2]/li[4]/a')

    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()

    driver.find_element_by_xpath('//*[@id="navbar-collapse-grid"]/ul[2]/li[4]/ul/li/div/div[1]/ul[3]/li[6]/a').click()
    #accept cookies
    driver.find_element_by_xpath('//*[@id="btnContinue"]').click()
    try:
        searchIframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="careersframe"]'))
        )
    except:
        driver.quit()
    driver.switch_to_frame(searchIframe)

    #filling the button search Job by ID
    driver.find_element_by_id('com.peopleclick.cp.formdata.SEARCHCRITERIA_CLIENTREQID').send_keys('55631')                     
    driver.find_element_by_xpath('//*[@id="sp-searchButton"]').click()
    try:
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="careersframe"]'))
        )
    except:
        print('nije nasao')
    driver.find_element_by_xpath('//*[@id="mobile_applybutton_124773_en-us"]').click()
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_AUTH_PRIMARYEMAILADDRESS"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_AUTH_PASSWORD"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="signinButton"]').click()
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.CAND_CONTACTMETHOD"]').click()
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.CAND_CONTACTMETHOD"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="nextButton"]').click()

    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.FLD_REGIONAL_SOURCE"]').click()
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.FLD_REGIONAL_SOURCE"]/option[13]').click()

    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.FLD_CAND_PERCENT_TRAVEL_ACCEPTABLE_DL"]').click()
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.FLD_CAND_PERCENT_TRAVEL_ACCEPTABLE_DL"]/option[12]').click()

    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.CAND_WORK_ELIGIBILITY"]').click()
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.CAND_WORK_ELIGIBILITY"]/option[2]').click()

    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.FLD_CP_PREV_SUNGARD_EMPLOYEE"]').click()
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.FLD_CP_PREV_SUNGARD_EMPLOYEE"]/option[3]').click()


    driver.find_element_by_xpath('//*[@id="nextButton"]').click()
    

    
    

except:
    print('puko')