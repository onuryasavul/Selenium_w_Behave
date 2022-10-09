import time
from behave import *
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

webdriver_path = "{}\chromedriver\chromedriver.exe".format(os.getcwd())

@given(u'launch browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(webdriver_path)


@when(u'open orangehrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")


@when(u'Enter username "{usr}" and password "{pw}"')
def step_impl(context, usr, pw):
    time.sleep(1)
    context.driver.find_element(By.NAME, "username" ).send_keys(usr)
    context.driver.find_element(By.NAME, "password" ).send_keys(pw)


@when(u'Click on login button')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH,
                                "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

@then(u'User must successfully login the Dashboard page')
def step_impl(context):
    time.sleep(1)

    assert context.driver.find_element(By.XPATH,
                                       "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6").text == "PIM"
    context.driver.close()