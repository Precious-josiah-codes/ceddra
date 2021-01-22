from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from bs4 import BeautifulSoup
import time
import random


class Music:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={self.user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', options=self.options)
        
        self.moods = {
            'sad': [
                {'song_name': 'When We Were Young', 'artiste': 'Adele'},
                {'song_name': 'Beyond', 'artiste': 'Leon Bridges'},
                {'song_name': 'Homesick', 'artiste': 'Dua Lipa'},
                {'song_name': 'Dancing on My Own', 'artiste': 'Calum Scott'},
                {'song_name': 'Be Alright', 'artiste': 'Dean Lewis'},
                {'song_name': 'You Say', 'artiste': 'Lauren Daigle'},
                {'song_name': 'The Scientist', 'artiste': 'Coldplay'},
                {'song_name': 'Past Life', 'artiste': 'Maggie Rogers'},
                {'song_name': 'Palace', 'artiste': 'Cam'},
                {'song_name': 'Hallucinations', 'artiste': 'dvsn'},
                {'song_name': 'A Thousand Years', 'artiste': 'Christina Perri'},
                {'song_name': 'i love you', 'artiste': 'billie eilish'},
                {'song_name': 'hostage', 'artiste': 'billie eilish'},
                {'song_name': 'lovely', 'artiste': 'billie eilish & khalid'},
            ],
            'happy': [
                {'song_name': 'Happy', 'artiste': 'Pharell williams'},
                {'song_name': 'cant stop the feeling', 'artiste': 'justin timberlake'},
                {'song_name': 'Better When Im Dancin', 'artiste': 'Meghan Trainor'},
                {'song_name': 'Its A Beautiful Day', 'artiste': 'Michael Bublé'},
                {'song_name': 'want to want me', 'artiste': 'Jason derulo'},
                {'song_name': 'Forever', 'artiste': 'Chris Brown'},
                {'song_name': 'Shake It Off', 'artiste': 'Taylor Swift'},
                {'song_name': 'All About That Bass', 'artiste': 'Meghan Trainor'},
                {'song_name': 'Everybodys Got Somebody But Me ft. Jason Mraz', 'artiste': 'Hunter Hayes'},
                {'song_name': 'Cheap Thrills', 'artiste': 'Sia ft. Sean Paul'}

            ],
            'romantic': [
                {'song_name': 'Thinking Out Loud', 'artiste': 'Ed Sheeran'},
                {'song_name': 'Perfect', 'artiste': 'Ed Sheeran'},
                {'song_name': 'All of Me', 'artiste': 'John Legend'},
                {'song_name': 'Say You Wont Let Go', 'artiste': 'James Arthur'},
                {'song_name': 'Halo', 'artiste': 'Beyoncé'},
                {'song_name': 'Stay', 'artiste': 'Rihanna ft. Mikky Ekko'},
                {'song_name': 'Love Someone', 'artiste': 'Lukas Graham'},
                {'song_name': 'Never Let You Go', 'artiste': 'Justin Bieber'},
                {'song_name': 'Adore You', 'artiste': 'Miley Cyrus'},
                {'song_name': 'Its Easier When Youre Standing There', 'artiste': 'Garrett Kato'}
            ],
            'gospel': [
                {'song_name': 'you waited', 'artiste': 'Travis greene'},
                {'song_name': 'made a way', 'artiste': 'Travis greene'},
                {'song_name': 'A Billion People', 'artiste': 'Deitrick Haddon & Hill City Worship Camp'},
                {'song_name': 'Rooftops', 'artiste': 'Jesus Culture'},
                {'song_name': 'Oceans', 'artiste': 'hillsosng united'},
                {'song_name': 'Way Maker', 'artiste': 'Leeland'},
                {'song_name': 'wekobiro', 'artiste': 'samsung'},
                {'song_name': 'The Blessing', 'artiste': 'Kari Jobe & Cody Carnes'},
                {'song_name': 'champion', 'artiste': 'bethel music'},
                {'song_name': 'Spirit Lead Me (Live)', 'artiste': 'Influence Music'}
 
                
            ]
        }
        
        
    def playMusic(self, music):
        search_query = f'https://music.youtube.com/search?q={music}'
        self.driver.implicitly_wait(5)
        self.driver.get(search_query)
        self.driver.find_element_by_xpath('//*[@id="chips"]/ytmusic-chip-cloud-chip-renderer[1]/a').click()
        try:
            play = self.driver.find_element_by_xpath('//*[@id="contents"]/ytmusic-responsive-list-item-renderer[1]/div[2]/div[1]/yt-formatted-string')
            seconds = self.timeFrame()
            play.click()
            ad = self.checkAd()
            if ad:
                self.muteMusic()
                self.skipAD()
                self.muteMusic()
                time.sleep(seconds)
                self.driver.quit()
            else:
                ad = self.checkAd()
                if ad:
                    self.muteMusic()
                    self.skipAD()
                    self.muteMusic()
                    time.sleep(seconds)
                    self.driver.quit()
                else:
                    time.sleep(seconds)
                    self.driver.quit()
        except StaleElementReferenceException:
            self.driver.refresh()
            time.sleep(5)

            play = self.driver.find_element_by_xpath('//*[@id="contents"]/ytmusic-responsive-list-item-renderer[1]/div[2]/div[1]/yt-formatted-string')
            seconds = self.timeFrame()
            play.click()
            ad = self.checkAd()
            

            if ad:
                self.muteMusic()
                self.skipAD()
                self.muteMusic()
                time.sleep(seconds)
                self.driver.quit()
            else:
                # check for ad here
                ad = self.checkAd()
                if ad:
                    self.muteMusic()
                    self.skipAD()
                    self.muteMusic()
                    time.sleep(seconds)
                    self.driver.quit()
                else:
                    time.sleep(seconds)
                    self.driver.quit()
        
    def playMood(self, mood):
        if mood == 'sad':
            random_songs = random.randint(1, len(self.moods['sad'])) - 1
            song = self.moods['sad'][random_songs]
            song_name = song['song_name']
            song_title = song['artiste']

            self.driver.get(f'https://music.youtube.com/search?q={song_name }+{song_title}')

            play = self.driver.find_element_by_xpath('//*[@id="contents"]/ytmusic-responsive-list-item-renderer[1]/div[2]/div[1]/yt-formatted-string/a')
            seconds = self.timeFrame()
            play.click()
            ad = self.checkAd()
            if ad:
                self.muteMusic()
                self.skipAD()
                self.muteMusic()
                time.sleep(seconds)
                self.driver.quit()
            else:
                ad = self.checkAd()
                if ad:
                    self.muteMusic()
                    self.skipAD()
                    self.muteMusic()
                    time.sleep(seconds)
                    self.driver.quit()
                else:
                    time.sleep(seconds)
                    self.driver.quit()
        elif mood == 'happy':
            random_songs = random.randint(1, len(self.moods['happy'])) - 1
            print('song index', random_songs)
            song = self.moods['happy'][random_songs]
            song_name = song['song_name']
            song_title = song['artiste']

            self.driver.get(f'https://music.youtube.com/search?q={song_name }+{song_title}')
            play = self.driver.find_element_by_xpath('//*[@id="contents"]/ytmusic-responsive-list-item-renderer[1]/div[2]/div[1]/yt-formatted-string/a')
            seconds = self.timeFrame()
            play.click()
            ad = self.checkAd()
            if ad:
                print('theres an AD')
                self.muteMusic()
                self.skipAD()
                self.muteMusic()
                time.sleep(seconds)
                self.driver.quit()
            else:
                print('No AD')
                ad = self.checkAd()
                if ad:
                    print('theres an AD')
                    self.muteMusic()
                    self.skipAD()
                    self.muteMusic()
                    time.sleep(seconds)
                    self.driver.quit()
                else:
                    print('sleeping code')
                    time.sleep(seconds)
                    self.driver.quit()
        elif mood == 'romantic':
            random_songs = random.randint(1, len(self.moods['romantic'])) - 1
            print('random number', random_songs)
            song = self.moods['romantic'][random_songs]
            # print('song index', random_songs, song)
            song_name = song['song_name']
            song_author = song['artiste']

            self.driver.get(f'https://music.youtube.com/search?q={song_name }+{song_author}')
            play = self.driver.find_element_by_xpath('//*[@id="contents"]/ytmusic-responsive-list-item-renderer[1]/div[2]/div[1]/yt-formatted-string/a')
            seconds = self.timeFrame()
            play.click()
            ad = self.checkAd()
            if ad:
                print('theres an AD')
                self.muteMusic()
                self.skipAD()
                self.muteMusic()
                time.sleep(seconds)
                self.driver.quit()
            else:
                print('No AD')
                ad = self.checkAd()
                if ad:
                    print('Theres an AD')
                    self.muteMusic()
                    self.skipAD()
                    self.muteMusic()
                    time.sleep(seconds)
                    self.driver.quit()
                else:
                    print('sleeping code')
                    time.sleep(seconds)
                    self.driver.quit()
        elif mood == 'gospel':
            random_songs = random.randint(1, len(self.moods['gospel'])) - 1
            print('random number', random_songs)
            song = self.moods['gospel'][random_songs]
            # print('song index', random_songs, song)
            song_name = song['song_name']
            song_author = song['artiste']

            self.driver.get(f'https://music.youtube.com/search?q={song_name }+{song_author}')
            play = self.driver.find_element_by_xpath('//*[@id="contents"]/ytmusic-responsive-list-item-renderer[1]/div[2]/div[1]/yt-formatted-string/a')
            seconds = self.timeFrame()
            play.click()
            ad = self.checkAd()
            if ad:
                print('theres an AD')
                self.muteMusic()
                self.skipAD()
                self.muteMusic()
                time.sleep(seconds)
                self.driver.quit()
            else:
                print('No AD')
                ad = self.checkAd()
                if ad:
                    print('Theres an AD')
                    self.muteMusic()
                    self.skipAD()
                    self.muteMusic()
                    time.sleep(seconds)
                    self.driver.quit()
                else:
                    print('sleeping code')
                    time.sleep(seconds)
                    self.driver.quit()
        else:
            print('not a sad song')

    def muteMusic(self):
        mute = self.driver.find_element_by_xpath('//*[@id="expand-volume"]')
        self.driver.execute_script("arguments[0].click();", mute) 

    def checkAd(self):
        time.sleep(1)
        page = self.driver.page_source
        soup = BeautifulSoup(page, 'lxml')
        ad = soup.find('div', class_='ad-showing')
        return ad

    def skipAD(self):
        try:
            ad_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="ad-text:7"]'))
            )
            ad_element.click()
        except:
            pass
    
    def timeFrame(self):
        time.sleep(5)
        page_src = self.driver.page_source
        bsoup = BeautifulSoup(page_src, 'lxml')
        get_time = bsoup.find('yt-formatted-string', class_='flex-column style-scope ytmusic-responsive-list-item-renderer complex-string') 
        music_time = get_time['title'].split()[-1]

        first_digit = music_time[0]
        second_digit = music_time[2:]

        seconds = int(first_digit) * 60 + int(second_digit)
        return seconds
    
    def quit(self):
        self.driver.quit()

