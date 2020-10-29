import requests
from bs4 import BeautifulSoup


def get_jobs():

    url = 'https://westernmass.craigslist.org/search/jjj?query=roofing'

    search = BeautifulSoup(requests.get(url).content, 'html.parser')

    # Grabs all listings
    listings = search.findAll("p", {"class": "result-info"})

    for listing in listings:

        # Title of Listing
        listing_title = listing.find("a", {"class": "result-title"})

        # Listing link
        listing_link = listing_title['href']

        # Date for program to use
        listing_datetime = listing.find("time", {"class": "result-date"})['datetime']

        # Date to display to human
        listing_date_title = listing.find("time", {"class": "result-date"})['title']

        # Neighborhood
        listing_hood = listing.find("span", {"class": "result-hood"})

        print(listing_link)
