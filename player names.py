from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

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

#print len(player_names)

add_link = "https://dak.gg"

for i in player_names:
	n = i.find('a')
	l = add_link + n['href'].rsplit('?r=na')[0] + '/2018-06/na/solo-fpp'
	player_list.append(l)

#print player_list

stats = []
listHead = ['name', 'bestRating', 'gamesPlayed', 'won', 'lost', 'winRatio', 'topTens', 'topTenRate',
		 'topTenWinRatio', 'killRating', 'highestKills', 'totalKills', 'headshots', 'headshotRatio', 'assists', 'k/d',
		 'vehiclesDestroyed', 'roadKills', 'longestKill', 'longestTimeSurvived', 'averageTimeSurvived', 
		 'averageDistanceTravelled', 'damageDealt', 'weaponsAcquired']
stats.append(listHead)

for link in player_list:

	driver.get(link)
	html_doc = driver.page_source
	soup = BeautifulSoup(html_doc, 'lxml')

	list1 = []
	list1.append((soup.find('span', class_ = 'nick')['data-nick']).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Season Best Rating').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Games').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Won').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Defeats').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'WinRatio').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Top10s').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Top10 Rate').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Top10 WinRatio').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Kill Rating').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Most Kills Per Game').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Kills').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Headshots').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Headshot Kill Ratio').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Assists').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'K/D').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Vehicles Destroyed').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Road Kills').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Longest Kill').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Longest Time Survived').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'AVG Time Alive').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'AVG Traveled').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Total Damage Dealt').find_next_sibling('dd').text).encode("utf-8"))
	list1.append((soup.find('dt', text = 'Weapons Acquired').find_next_sibling('dd').text).encode("utf-8"))
	stats.append(list1)

print stats

with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(stats)
driver.quit()