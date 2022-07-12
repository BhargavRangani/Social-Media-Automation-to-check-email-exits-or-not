import requests
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=options)

def twitter_auth(email_id):
    print("Please wait while we verify the email...")
    driver.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D")
    sleep(15)
    try:
        email_input = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
    except:
        print("Error: The twitter API reported an error loading the page! Please re-run the script")
    
    email_input.send_keys(email_id)
    sleep(2)
    next_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
    next_button.click()
    sleep(3)
    
    try:
        #done = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div')
        done = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div[1]/span')
        if done:
            return 0
    except:
        return 1
def facebook_auth(email_id):
            print("Please wait while we verify the email with Facebook...")
            driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
            sleep(15)
            try:
                email_input = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/form/div/div[2]/div/table/tbody/tr[2]/td[2]/input')
            except:
                print("Error: The facebook API reported an error loading the page! Please re-run the script")
            
            email_input.send_keys(email_id)
            sleep(2)
            next_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/form/div/div[3]/div/div[1]/button')
            next_button.click()
            sleep(3)
            
            try:
                sorry = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/form/div/div[2]/div[1]')
                if sorry:
                    return 0
            except:
                return 1
def linkedin_auth(email_id):
            print("Please wait while we verify the email with Linkedin...")
            driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
            sleep(10)
            try:
                email_input = driver.find_element(By.XPATH,'//*[@id="username"]')
                login_password_element = driver.find_element(By.XPATH,'/html/body/div/main/div[2]/div[1]/form/div[2]/input')
                login_password_element.send_keys("123456")
            except:
                print("Error: The linkedin API reported an error loading the page! Please re-run the script")
            
            email_input.send_keys(email_id)
            sleep(2)
            reset_button = driver.find_element(By.XPATH,'/html/body/div/main/div[2]/div[1]/form/div[3]/button')
            reset_button.click()
            sleep(3)
            
            try:
                sorry = driver.find_element(By.XPATH,'/html/body/div/main/h1')
                if sorry:
                    return 0        
            except:
                yes = driver.find_element(By.XPATH,'/html/body/div/main/div[2]/div[1]/form/div[2]/div')
                if yes:
                    return 1

email_input = input("Enter an email: ")
print("For which social media handle you want to check?")
def menu():
    print("Press [1] for Twitter")
    print("Press [2] for Facebook")
    print("Press [3] for Linkedin")

menu()
option = int(input("Please choose your option: "))
while option !=0:
    if option == 1:   
        success = twitter_auth(email_input)
        if(success==1):
            print("Email id is registered with Twitter")
        else:
            print("There is no account with the provided email registered on Twitter")
        break;
    elif option == 2:            
        success = facebook_auth(email_input)
        if(success==1):
            print("Email id is registered with Facebook")
        else:
            print("There is no account with the provided email registered on Facebook")
        break;
        break;
    elif option == 3:
        success = linkedin_auth(email_input)
        if(success==1):
            print("Email id is registered with Linkedin")
        else:
            print("There is no account with the provided email registered on Linkedin")
        break;
    else:
        print("Invalid Input")

driver.close()
