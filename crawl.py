import requests
from bs4 import BeautifulSoup as bs

url = 'https://westernmass.craigslist.org/search/apa'
gig_url = 'https://westernmass.craigslist.org/search/ggg'

gig_locations = {
    # 'Western Mass': 'https://westernmass.craigslist.org/search/ggg',
    # 'Boston': 'https://boston.craigslist.org/search/ggg',
    # 'New York': 'https://newyork.craigslist.org/search/ggg',
    # 'Philadelphia': 'https://philadelphia.craigslist.org/search/ggg'
}

complete_list = []

visited = []

city_queue = []


###############################################

count = 0

def crawlyboi(starting_point=None):
    global count
    count+=1
    if count > 900:
        print(complete_list)
        return
    # If user specifies starting point, use that - otherwise start in boston
    if not starting_point:
        starting_point = 'https://boston.craigslist.org/search/ggg'

        # Get content of the starting point
        starting_page = bs(requests.get(starting_point).content, 'html.parser')

        #run data collection code here
        gig_search(search_terms, starting_point, 3)

        values = starting_page.select('#areaAbb > option')

        local_list = []

        for value in values:
            local_list.append(value['value'])

        for city in local_list:
            city_queue.append(city)

        # At this point this page's values have been sorted and data has been collected and we are ready to move to the next city

        crawlyboi(city_queue[0])

    else:
        starting_point = 'https://' + starting_point + '.craigslist.org/search/ggg'

        # Get content of the starting point
        starting_page = bs(requests.get(starting_point).content, 'html.parser')

        # run data collection code here
        gig_search(search_terms, starting_point, 3)

        values = starting_page.select('#areaAbb > option')

        local_list = []

        for value in values:
            local_list.append(value['value'])

        visited.append(city_queue[0])
        city_queue.remove(city_queue[0])

        for city in local_list:
            if city not in visited and city not in city_queue:
                # If the city is new and hasn't been queued, add to queue - NN
                count += 1
                city_queue.append(city)
            # If the city has been searched, ignore
            if city in visited and city not in city_queue:
                # - YN
                count += 1
                pass
            if city in visited and city in city_queue:
                # If the city is accidentally in both lists, remove from queue - YY
                count += 1
                city_queue.remove(city)
            if city not in visited and city in city_queue:
                # If the city has already been queued, kill - NY
                count += 1
                break

            count += 1
        count += 1

        # At this point this page's values have been sorted and data has been collected and we are ready to move to the next city
        crawlyboi(city_queue[0])



pages = {
    1: '?',
    2: '?s=120',
    3: '?s=240'
}

search_terms = [
    'wordpress', 'Wordpress', 'WordPress', 'word press', 'Word press', 'Word Press'
]

soup = bs(requests.get(url).content, 'html.parser')

# I want to create a large program that checks every city in the US for listings that match my criteria
# Loop through each page, create a queue of potential cities connected to that particular node,
# check to see if the cities are in another queue or have been ran yet.
# Look into threading in order to check queues and add/not add conflicting cities

# break the functionality into separate functions.
# (e.g. search the page for keywords, queue up other cities and check against the current queue)


def gig_search(terms, intended_url, page_count=None):

    if page_count:
        counter = 0
        for key, value in pages.items():
            if key == counter:
                break
            else:
                if key <= 1:
                    var = bs(requests.get(intended_url).content, 'html.parser')
                    titles = var.findAll("a", {"class": "result-title"})
                    print(intended_url)

                    for single in titles:
                        # For all anchor tags on the page
                        for term in terms:
                            # For each term the user specified
                            if term in single.text:
                                # If the term is in the title of the listing
                                complete_list.append(single['href'])
                    counter += 1
                else:
                    # For the remaining pages
                    var = bs(requests.get(intended_url + pages[key]).content, 'html.parser')
                    titles = var.findAll("a", {"class": "result-title"})

                    for single in titles:
                        for term in terms:
                            if term in single.text:
                                complete_list.append(single['href'])


    # for name, url in locations.items():
    #     if page_count:
    #         # if the user specifies an amount of pages to search
    #         counter = 0
    #         for key, value in pages.items():
    #             # for each page
    #             if key == counter:
    #                 # I actually don't have any idea if this does anything, but I'm too scared to check
    #                 break
    #             else:
    #                 if key <= 1:
    #                     # For the first page
    #                     var = bs(requests.get(url).content, 'html.parser')
    #                     titles = var.findAll("a", {"class": "result-title"})
    #
    #                     print('\n')
    #                     print('------------------------------------------------')
    #                     print('\n')
    #                     print(name + ': page ' + str(key))
    #
    #                     for single in titles:
    #                         # For all anchor tags on the page
    #                         for term in terms:
    #                             # For each term the user specified
    #                             if term in single.text:
    #                                 # If the term is in the title of the listing
    #                                 print(single.text)
    #                                 print(single['href'])
    #                                 complete_list.append(single['href'])
    #                     counter += 1
    #                 else:
    #                     # For the remaining pages
    #                     var = bs(requests.get(url + pages[key]).content, 'html.parser')
    #                     titles = var.findAll("a", {"class": "result-title"})
    #
    #                     print('\n')
    #                     print('------------------------------------------------')
    #                     print('\n')
    #                     print(name + ': page ' + str(key))
    #
    #                     for single in titles:
    #                         for term in terms:
    #                             if term in single.text:
    #                                 print(single.text)
    #                                 print(single['href'])
    #                                 complete_list.append(single['href'])

    # print(complete_list)



# def gig_search(terms, locations, page_count=None):
#
#     complete_list = []
#
#     print('thinking...')
#     for name, url in locations.items():
#         if page_count:
#             # if the user specifies an amount of pages to search
#             counter = 0
#             for key, value in pages.items():
#                 # for each page
#                 if key == counter:
#                     # I actually don't have any idea if this does anything, but I'm too scared to check
#                     break
#                 else:
#                     if key <= 1:
#                         # For the first page
#                         var = bs(requests.get(url).content, 'html.parser')
#                         titles = var.findAll("a", {"class": "result-title"})
#
#                         print('\n')
#                         print('------------------------------------------------')
#                         print('\n')
#                         print(name + ': page ' + str(key))
#
#                         for single in titles:
#                             # For all anchor tags on the page
#                             for term in terms:
#                                 # For each term the user specified
#                                 if term in single.text:
#                                     # If the term is in the title of the listing
#                                     print(single.text)
#                                     print(single['href'])
#                                     complete_list.append(single['href'])
#                         counter += 1
#                     else:
#                         # For the remaining pages
#                         var = bs(requests.get(url + pages[key]).content, 'html.parser')
#                         titles = var.findAll("a", {"class": "result-title"})
#
#                         print('\n')
#                         print('------------------------------------------------')
#                         print('\n')
#                         print(name + ': page ' + str(key))
#
#                         for single in titles:
#                             for term in terms:
#                                 if term in single.text:
#                                     print(single.text)
#                                     print(single['href'])
#                                     complete_list.append(single['href'])
#
#     print(complete_list)


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


# gig_search(search_terms, 'https://philadelphia.craigslist.org/search/ggg', 2)


crawlyboi()
