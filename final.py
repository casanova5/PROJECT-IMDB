''' Top 100 most popular TV show'''

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

table=soup.find('tbody', class_="lister-list")

show = []
show_star = []
year = []
rating = []


for row in table.findAll("tr"):
    cells = row.findAll('td')
    show.append(cells[1].find('a').get_text())                #get_text to get text in between the tags
    show_star.append(cells[1].find('a')['title'])
    year.append(cells[1].find('span').get_text())
    rating.append(cells[2].find('strong').get_text())

IMDB = pd.DataFrame(
    {
        'show name': show,
        'starring': show_star,
        'year':year,
        'rating': rating,
    }) 

print(IMDB)

IMDB.to_csv('IMDB.csv')

