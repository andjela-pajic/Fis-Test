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
    
    #hover over menu to select carreers
    element_to_hover_over = driver.find_element_by_xpath('//*[@id="navbar-collapse-grid"]/ul[2]/li[4]/a')
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()

    driver.find_element_by_xpath('//*[@id="navbar-collapse-grid"]/ul[2]/li[4]/ul/li/div/div[1]/ul[3]/li[6]/a').click()
    #accept cookies
    driver.find_element_by_xpath('//*[@id="btnContinue"]').click()
    #wait for the iframe to load
    try:
        searchIframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="careersframe"]'))
        )
    except Exception as e:
        print('Iframe not found')
        print(e)
    #switch context to the iframe
    driver.switch_to_frame(searchIframe)

    #filling the button search Job by ID
    driver.find_element_by_id('com.peopleclick.cp.formdata.SEARCHCRITERIA_CLIENTREQID').send_keys('55631')                     
    driver.find_element_by_xpath('//*[@id="sp-searchButton"]').click()
    #wait for new page to load
    try:
        applyButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mobile_applybutton_124773_en-us"]'))
        )
    except Exception as e:
        print('Button not found')
        print(e)
    applyButton.click()
    #filling the input for email
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_AUTH_PRIMARYEMAILADDRESS"]').send_keys(email)
    #filling the input for username
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
    #wait for the next page
    try:
        uploadResumeField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="resumeFile"]'))
        )
    except Exception as e:
        print('Upload button not found')
        print(e)
    #upload resume
    uploadResumeField.send_keys(os.getcwd() + r"\Andjela_Pajic_CV.pdf")

    #check radio button for uploading cover letter
    driver.find_element_by_xpath('//*[@id="uploadCLRadio-label"]').click()
    #upload cover letter   
    driver.find_element_by_xpath('//*[@id="coverLetterFile"]').send_keys(os.getcwd() + r"\Andjela_Pajic_cover_letter.pdf")

    driver.find_element_by_xpath('//*[@id="nextButton"]').click()
    driver.find_element_by_xpath('//*[@id="nextButton"]').click()
    driver.find_element_by_xpath('//*[@id="nextButton"]').click()

    driver.find_element_by_xpath('//*[@id="id-com.peopleclick.cp.formdata.FLD_CP_CONSENT_STATEMENT-1"]').click()
    driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.FLD_CP_CONSENT_USERNAME"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="finishButton"]').click()

except Exception as e:
    print('Something goes wrong')
    print(e)