# PUBG-data
A scrape of dak.gg, which is a PUBG (PlayerUnknown's Battlegrounds) leaderboard website, to gather player statistics and explore the generated dataset

## Scraping The Data
The goal is to scrape the data for the top 100 solo-FPP players of the 2018-06 season. A list of top 100 solo-FPP players is available at this link: https://dak.gg/ranks/na/solo-fpp/rating  
We will be using Selenium along with PhantomJS for accessing the webpages and BeautifulSoup for parsing the HTML data.  
First, we visit this link and gather the url for each of the top 100 players' profile page and store them in a list. Then, we visit each link and gather the individual player stats from them, storing them in a list called stats. Finally, we use the csv module to write the files to the storage as a csv (comma separated values) file.  