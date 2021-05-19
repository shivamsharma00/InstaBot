# This class login in the instagram.

from time import sleep


class LoginPage:
    

    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

    def login(self, username, password):
        username_input = self.browser.find_element_by_name('username')
        password_input = self.browser.find_element_by_name('password')

        username_input.send_keys(username)
        password_input.send_keys(password)

        sleep(5)

        self.browser.find_element_by_xpath("//button[@type='submit']").click()

        return self.browser
