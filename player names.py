from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

class Player():
	def __init__(self):
		self.name = ""
		self.link = ""

player_list = []

driver = webdriver.PhantomJS(executable_path = r'C:\Users\sarim\Desktop\Scraper\phantomjs.exe')
driver.get('https://dak.gg/ranks/na/solo-fpp/rating')
pause = 0
lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight

html_doc = driver.page_source
soup = BeautifulSoup(html_doc, 'lxml')

players = soup.find('table', class_ = 'list rating')
player_names = players.find_all('td', class_ = 'nick')

add_link = "https://dak.gg"

for i in player_names[0:3]:
	newPlay = Player()
	n = i.find('a')
	l = add_link + n['href']
	newPlay.link = l
	newPlay.name = n.text.strip()
	print newPlay.name
	print newPlay.link
	player_list.append(newPlay)

#print players_names[1]
driver.quit()