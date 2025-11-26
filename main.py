import time
import os
import sys
import re
import argparse
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class __init__:
    """
        only compatible with windows
        version:0.11
        Need Chrome

        Webbot
        
        Author: UnexpectedUser
    """

class main:
    parser = argparse.ArgumentParser(description='Simple Web Bot')
    parser.add_argument('url', metavar='url', type=str, help='The URL To Enter With')
    parser.add_argument('choice', metavar='choice', type=str, help='1: open a website \n 2: open a website and login (Username and Password) \n 3: Get website page source')
    args = parser.parse_args()
    url = args.url
    choice = args.choice
    osType = sys.platform
    
    if osType=='win32':
        pass
    else:
        print('Not compatible with that os only windows 10 or 11')
        print('Timeout(exit)')
        exit()
    
    if choice=='1':
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path = 'C:\ProgramFiles\Google\Chrome\Application\chrome.exe', chrome_options=chrome_options)
        driver.get(url)

    if choice=='2':
        
        username = input('Whats The Username: ')
        password = input('\nWhats The Password: ')
        
        usernameField = input('\nWhats The Username Field:')
        passwordField = input('\nWhats The Password Field:')
        cssEnterlogin = input('\nWhats The Css Field For The Login Button: ')
        
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome('C:\ProgramFiles\Google\Chrome\Application\chrome.exe', chrome_options=chrome_options)
        driver.get(url)

        driver.find_element_by_name().send_keys(username)
        driver.find_element_by_name().send_keys(password)
        driver.find_element_by_css_selector(cssEnterlogin).click()

        print("[+] Logged IN")

    if choice=='3':
        saveFile=input('Would You like to store the code in a file y/n: ')
        
        if saveFile=='y':
            req = requests.get(url)
            if req.status_code==200:
                try:
                    webGet = requests.get(url)
                except requests.exceptions as ErrorWeb:
                    print('[-] error in website')
                    print(ErrorWeb)
                except requests.exceptions.MissingSchema as urlE:
                    print('Needs https://[url].com')
                    print(urlE)
                    
                try:
                    file=input('\nWhat is the name of the file you wanna save it in: ')
                    mkFile = open(file, 'x')
                    mkFile.write(str(webGet.content))
                except FileExistsError as error:
                    print('[-] There was an error')
                    print(error)
                except InterruptedError as error:
                    print('[-] There was an error')
                    print(error)
                    
                print('[+] Saved In File')
            else:
                print('Url not avalible')
                print('Exit Timeout(0)')
                exit()
        else:
            req = requests.get(url)
            
            if req.status_code==200:
                webGet = requests.get(url)
                print(str(webGet.content))
            else:
                print('Url not avalible')
                print('Exit Timeout(0)')
                exit()

