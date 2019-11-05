# https://bit.ly/2NyxdAG
from bs4 import BeautifulSoup
import requests
import re

# Download IMDB's Top 250 data
url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')

links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
#print(links)
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []

for link in links:
    newurl = 'https://www.imdb.com'+link
    response=requests.get(newurl)
    #print("hello")
    soup1 = BeautifulSoup(response.text,'lxml')
#    maintitle=soup1.select('.title_wrapper')
    maintitle=[a.string for a in soup1.select('.title_wrapper h1')]
    print(maintitle)

    rating = [a.attrs.get('title') for a in soup1.select('.ratingValue strong')]
    print(rating)
    releasedate= [a.string for a in soup1.select('.subtext a')]
    releasedate=releasedate[-1]
    print(releasedate)
    datetie = [a.string for a in soup1.select('.subtext time')]
    print(datetie)
    summarytext = [c.string for c in soup1.select('.summary_text')]
    print(summarytext)

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index)) - (len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    imdb.append(data)

#for item in imdb:
 #   print(item['place'], '-', item['movie_title'], '(' + item['year'] + ') -', 'Starring:', item['star_cast'])
