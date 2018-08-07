import os
import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

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
    driver.find_element_by_xpath('//*[@id="registerButton"]').click()
    #filling the input for e-mail
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_AUTH_PRIMARYEMAILADDRESS"]').send_keys('andjela.pajic90@gmail.com')
    #filling the input for password
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_AUTH_PASSWORD"]').send_keys('pile2707')
    #reentering password
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_AUTH_REENTER_PASSWORD"]').send_keys('pile2707')
    #filling the input for first name
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_FIRSTNAME"]').send_keys('Anđela')
    #reentering first name
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.FLD_USER_PREFERRED_FIRST_NAME"]').send_keys('Anđela')
    #filling the input for last name
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_LASTNAME"]').send_keys('Pajić')
    #reentering last name
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.FLD_USER_PREFERRED_LAST_NAME"]').send_keys('Pajić')
    #filling the input for address
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_ADDRESS1"]').send_keys('Jurija Gagarina')
    #filling the input for city
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_CITY"]').send_keys('Belgrade')
    #choosing option for country
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_COUNTRYCODE"]').click()
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_COUNTRYCODE"]/option[192]').click() 
    #filling the input for postal code
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_POSTALCODE"]').send_keys('11070')
    #choosing option for country for mobile phone
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_MOBILEPHONE__COUNTRY"]').click()
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_MOBILEPHONE__COUNTRY"]/option[195]').click()
    #filling the input for mobile phone
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_MOBILEPHONE__PHONE"]').send_keys('638879132')
    #choosing option for state
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_STATEPROVINCE"]').click()
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_STATEPROVINCE"]/option[2]').click()

    driver.find_element_by_xpath('//*[@id="registerButton"]').click()
    
    driver.switch_to_frame(iframe)
    
    

except:
    print('puko')