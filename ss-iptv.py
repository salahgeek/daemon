from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openx import code
import time

class IptvBot:
    def __init__(self,btn,itmes,m3u,image,logo):
        self.btn = btn
        self.itmes = itmes
        self.m3u = m3u
        self.image = image
        self.logo = logo
        self.bot = webdriver.Firefox()
           
    def login(self):
        bot = self.bot
        bot.get('https://ss-iptv.com/en/users/playlist')
        time.sleep(3)
        #popup = bot.find_element_by_class_name('btn btn-success popup-modal-dismiss').click()
        #time.sleep(1)
        btn = bot.find_element_by_id('inptConnectionCodeInput')
        btn.send_keys(self.btn)
        time.sleep(2)
        
        btn2 = bot.find_element_by_id('btnAddDevice')   
        time.sleep(1)
        btn2.send_keys(Keys.RETURN)
        time.sleep(3)
        
        btn3 = bot.find_element_by_id('playlistsTab')
        btn3.click()
        time.sleep(2)
        
        btn3 = bot.find_element_by_id('btnClear').click()
        btnSave2 = bot.find_element_by_id('btnSave')
        btnSave2.click()
        #btnsave = bot.find_element_by_id('btnSave').click()
        time.sleep(3)

        image = bot.find_element_by_id('btnAddPlaylistItem').click()
        time.sleep(2)

        itmes = bot.find_element_by_id('inputStreamTitle')
        itmes.clear()
        itmes.send_keys(self.itmes)
        time.sleep(3)
        #---------------------------------

        #m3u.switch_to_frame(0)
        #m3u = bot.find_element_by_id('btnOpen').click().send_keys("C://Users//Daemon//Desktop//iptv.m3u").click()
        #m3u.send_keys(Keys.RETURN)
        #time.sleep(2)
        # -----------------------------------

        m3u = bot.find_element_by_id('inputStreamURL')
        m3u.send_keys(self.m3u)
        #m3u.send_keys(Keys.RETURN)
        time.sleep(2)

        image = bot.find_element_by_id('inputBackground')
        image.send_keys(self.image)
        #image.send_keys(Keys.RETURN)
        time.sleep(2)

        logo = bot.find_element_by_id('inputLogoURL')
        logo.send_keys(self.logo)
        #logo.send_keys(Keys.RETURN)
        time.sleep(2)

        btnSave1 = bot.find_element_by_id('btnApplyChanges')
        btnSave1.click()
        time.sleep(0.5)

        btnSave2 = bot.find_element_by_id('btnSave')
        btnSave2.click()
        time.sleep(5)
        bot.close()


ed = IptvBot(code,'SalahGentlMan','https://raw.githubusercontent.com/salahGentlMan/iptv/main/iptv.m3u','https://raw.githubusercontent.com/salahGentlMan/iptv/main/iptv.m3u','https://raw.githubusercontent.com/salahGentlMan/iptv/main/iptv.m3u')
ed.login()

#http://free24ip.xyz:8000/get.php?username=76661610975278&password=123&type=m3u_plus&output=mpegts
#http://free24ip.xyz:8000/get.php?username=2661610998957&password=123&type=m3u_plus&output=mpegts
#https://raw.githubusercontent.com/salahGentlMan/iptv/main/iptv.m3u