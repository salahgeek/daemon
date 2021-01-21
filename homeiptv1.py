from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
######################################################################## 
#                     Name: SALAH GENTL MAN                            #
#                     Email:salahgentlman@gmail.com                    #
#                                 :)                                   #
#                                                                      #
########################################################################

class homeiptv:
    def __init__(self,tvIdDel,tvId,m3_url):
        self.tvIdDel = tvIdDel
        self.tvId = tvId
        #self.m3ufile = m3ufile
        self.m3_url = m3_url
        self.bot = webdriver.Firefox()

    def automation(self):
        bot = self.bot
        bot.get('https://homeiptv.com/')
        time.sleep(4)

        popup = bot.find_element_by_id('onesignal-slidedown-cancel-button').click()
        time.sleep(0.5)

        uploadBTN = bot.find_element_by_xpath('/html/body/header[2]/div/nav/ul/li[3]/a').click()
        time.sleep(2)

        tvIdDel = bot.find_element_by_name('tvIdDel')
        tvIdDel.send_keys(self.tvIdDel)
        time.sleep(2)
       
        deletBTN = bot.find_element_by_xpath('//*[@id="finder-form-delete"]/button').click()
        time.sleep(4)
     
        tvId = bot.find_element_by_name('tvId')
        tvId.send_keys(self.tvId)

        time.sleep(2)

        #m3ufile = bot.find_element_by_name('file').send_keys('C:/Users/Daemon/Desktop/iptv.txt').click()
        
        m3_url = bot.find_element_by_name('m3_url')
        m3_url.send_keys(self.m3_url)
        time.sleep(2)
        
        SaveBTN = bot.find_element_by_xpath('//*[@id="finder-form-import"]/div/div[2]/div[3]/button').click()
        tvId.clear()
        time.sleep(5)
        bot.close()
#salah = homeiptv('6008949af2da8','6008949af2da8','https://raw.githubusercontent.com/salahGentlMan/iptv/main/iptv.m3u'
salah = homeiptv('5f2eff1b1a1dd','5f2eff1b1a1dd','https://raw.githubusercontent.com/salahGentlMan/iptv/main/iptv.m3u')
salah.automation()


#home Code Tv 1 :'5f2eff1b1a1dd'
#home Code Tv 2 :'6008949af2da8'