import requests
from bs4 import BeautifulSoup


def cnn(keyword, sites):
    titlefound = []
    url = 'https://www.cnn.com/world'
    soup = BeautifulSoup(requests.get(url).content, "lxml")
    articles = soup.find_all('h3', {'class': 'cd__headline'})

    print('Here are some articles on {} containing the word \'{}\':'.format(sites, keyword))
    print('\n')

    for article in articles:
        title = article.find('span').text
        link = article.find('a')['href']
        if keyword in title:
            if title not in titlefound:
                if 'http' not in link:
                    print(title, 'http://www.cnn.com' + link)
                    titlefound.append(title)
                else:
                    print(title, link)
                    titlefound.append(title)
            elif title in titlefound:
                continue

    if len(titlefound) == 0:
        print('Whoops! Sorry about that, it looks like your search came up empty!')


def npr(keyword, sites):
    url = 'https://www.npr.org/sections/news/'
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    kw = keyword.title()
    titleforfound = []  # Arbitrary list to help determine if the program has found anything
    articles = soup.find_all('article', {'class': 'item has-image'})

    print('Here are some articles on {} containing the word \'{}\': '.format(sites, keyword))
    print('\n')

    for article in articles:  # This singles out each individual post in a collection of posts (articles)
        title = article.find('h2').find('a').text  # This specifies that I want the title only, no HTML
        link = article.find('a')['href']  # This finds the link of the specific article
        if kw in title:  # this analyzes the titles and compares the keyword to each individual word
            print(title, '~', link)
            titleforfound.append(title)  # adding to list to let the program know something has been found

    if len(titleforfound) == 0:  # if the program didn't find anything
        print('Whoops! Sorry about that, it looks like your search came up empty!')


def fox(keyword, sites):
    url = 'https://www.cnn.com/world'  # url that is being scraped
    soup = BeautifulSoup(requests.get(url).content, "lxml")  # retrieves content from the url
    titlefound = []
    articles = soup.find_all('h3', {'class': 'cd__headline'})

    print('Here are some articles on {} containing the word \'{}\':'.format(sites, keyword))
    print('\n')

    for article in articles:
        title = article.find('span').text
        link = article.find('a')['href']
        if keyword in title:
            if title not in titlefound:
                if 'http' not in link:
                    print(title, 'http://www.cnn.com' + link)
                    titlefound.append(title)
                else:
                    print(title, link)
                    titlefound.append(title)
            elif title in titlefound:
                continue

    if len(titlefound) == 0:
        print('Whoops! Sorry about that, it looks like your search came up empty!')