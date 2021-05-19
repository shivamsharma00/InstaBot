# This class does the searching for hashtag, following, and liking the post.

import time
from time import sleep
from bs4 import BeautifulSoup as bs


class HomePage:


    def __init__(self, browser):
        self.browser = browser
        self.hashtags = []
        self.people_followed = []
        self.followed = 0
        self.likes = 0
        self.comment = 0
        self.comments = {1 :'yay', 2 : 'Awsome', 3 : 'Cool', 4 : 'Nice Pic', 5 : 'A True Natural Beauty'}
    
    def notification_click(self):
        self.browser.find_element_by_xpath("//*[contains(text(), 'Not Now')]").click()

    def like_pic(self):
        # sleep(2)
        like = self.browser.find_element_by_xpath("//*[contains(@class, 'fr66n')]")
        soup = bs(like.get_attribute('innerHTML'), 'html.parser')

        if (soup.find('svg')['aria-label']=='Like'):
            like.click()
            self.likes +=1
        # sleep(4)
        return 0
    
    def next_pic(self):
        sleep(2)
        try:
            nex = self.browser.find_element_by_xpath("//*[contains(@class, ' _65Bje  coreSpriteRightPaginationArrow')]")
            nex.click()
            sleep(5)
        except:
            pass
        return 0
    
    def follow(self, hashtag_list): 
        for hashtag in hashtag_list:
            self.browser.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
            sleep(5)

            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div').click()
            sleep(2)

            try:
                for x in range(1, 100):
                    first_post = self.browser.find_element_by_xpath("//*[contains(@class, 'sqdOP yWX7d     _8A5w5   ZIAjV ')]").text
                    if first_post not in self.people_followed:
                        if self.browser.find_element_by_xpath('//*[@class="sqdOP yWX7d    y3zKF     "]').text == 'Follow':
                            self.browser.find_element_by_xpath('//*[@class="sqdOP yWX7d    y3zKF     "]').click()
                            sleep(2)
                            
                            self.people_followed.append(first_post)
                            self.followed += 1
                            
                            self.like_pic()
                            # n = random.randint(1, 10)
                            # print('random number-', n)
                            
                            # if n < 6:
                            #     comnt = self.browser.find_element_by_xpath('//*[@class="Ypffh"]')
                            #     comnt.send_keys(self.comments[n])
                            #     comnt.send_keys(Keys.ENTER)
                            #     sleep(5)
                            #     self.comment +=1 
                    self.next_pic()
            except:
                continue
        
        file_name = '{}'.format(time.strftime("%Y%m%d-%H%M%S"))+'.txt'
        print(file_name)
        with open(file_name, 'w+') as w:
            for p in self.people_followed:
                w.write(p+'\n')
        w.close()
        print('Liked {} photos'.format(self.likes))
        print('Followed {} people'.format(self.followed))
        print('Commented {} people'.format(self.comment))

