import requests
from bs4 import BeautifulSoup as bs

url = 'https://westernmass.craigslist.org/search/apa'
soup = bs(requests.get(url).content, 'html.parser')


def craigslistSearch(min_price, max_price):

    for listing in soup.find_all('li', {'class':'result-row'}):

        title = listing.find('p').find('a').text
        price = listing.find('span', {'class':'result-price'}).text
        cleanPrice = int(price.replace('$', ''))
        legitPrice = ''
        link = listing.find('a')['href']

        if cleanPrice > max_price or cleanPrice < min_price:
            continue
        else:
            legitPrice += str(cleanPrice)

        print('Listing: ', title, '\n', 'Price: ', legitPrice, '\n', link, '\n'*2)


craigslistSearch(0, 900)


