# This class checks Not Now button for the notification which says to get notification on desktop.

from selenium import webdriver

class Check:
    
    def __init__(self, browser):
        self.browser = browser

    def click_notif_not_now(self):
        self.browser.find_element_by_xpath("//*[contains(text(), 'Not Now')]").click()
        return self.browser
