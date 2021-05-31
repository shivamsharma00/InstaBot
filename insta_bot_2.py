# To read selenium docs
# https://selenium-python.readthedocs.io/locating-elements.html

from selenium import webdriver
from bs4 import BeautifulSoup as bs
from login_insta import LoginPage
from notif_checker import Check
from home_insta import HomePage

if __name__ == '__main__':
    hastg = []
    num = int(input('Enter total number of Hashtags to follow: '))
    
    for i in range(num):
        hastg.append(input('Enter Hashtag: '))
    
    username = input('Enter Username: ')
    password = input('Enter Password: ')

    print("Initializing Bot...")

    browser = webdriver.Firefox()
    browser.implicitly_wait(5)

    login_page = LoginPage(browser)
    notif = Check(login_page.login(username=username, password=password))
    
    home = HomePage(notif.click_notif_not_now())
    home.notification_click()
    home.follow(hastg)

# passswd - cN@#$B=^pc3,Q"P
# https://github.com/shivamsharma00/InstaBot.git