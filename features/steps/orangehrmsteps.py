import time
from behave import *
from selenium import webdriver
import os
from selenium.webdriver.common.by import By


webdriver_path = "{}\chromedriver\chromedriver.exe".format(os.getcwd())

@given(u'launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(webdriver_path)


@when(u'open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then(u'verify that the logo is present on the page')
def verifyLogo(context):
    time.sleep(1)
    status = context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[1]/img").is_displayed()
    assert status is True
@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
