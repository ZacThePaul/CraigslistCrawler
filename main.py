import requests
from bs4 import BeautifulSoup

class Crawler:
	def __init__(self):
		self.results = []
		self.visited = []
		self.queue = []
		self.counter = 1
		self.pages = {1: '?', 2: '?s=120', 3: '?s=240'}
		self.complete_list = {}

	def gig_search(self, intended_url,  terms, today=None):

		for single_term in terms:

			# If user chooses listings from today, append to url
			new_url = intended_url + '?query=' + single_term + '&is_paid=yes&postedToday=1' if today else intended_url + '?query=' + single_term + '&is_paid=yes'

			var = BeautifulSoup(requests.get(new_url).content, 'html.parser')
			titles = var.findAll("a", {"class": "result-title"})

			for listing in titles:
				self.complete_list[listing.text] = (listing['href'])

	def home_search(self, intended_url, min_price, max_price):

		new_url = intended_url + '?min_price=' + str(min_price) + '&max_price=' + str(max_price)  + '&pets_cat=1'

		soup = BeautifulSoup(requests.get(new_url).content, 'html.parser')

		titles = soup.findAll("a", {"class": "result-title"})

		print(new_url)

		for title in titles:
			print(title.text + ' : ' + title['href'])

	def sort_cities(self, starting_point):

		print('Counter = ' + str(self.counter))
		if self.counter == 25:
			print(self.complete_list)
		if self.counter == 50:
			print(self.complete_list)
		if len(self.queue) < 2:
			print(self.complete_list)

		print('------------------------------------------------------')
		print(starting_point)
		print('VISITED: ', self.visited)
		print('QUEUED', self.queue)

		if self.counter == 30:
			print(self.complete_list)
		if self.counter == 50:
			print(self.complete_list)
		if self.counter == 75:
			print(self.complete_list)
		if self.counter == 100:
			print(self.complete_list)

		starting_url = 'https://' + starting_point + '.craigslist.org/search/ggg'

		# Grab the content!
		self.gig_search(starting_url, ['WordPress'])

		# Gets all HTML from desired page
		starting_content = BeautifulSoup(requests.get(starting_url).content, 'html.parser')

		# Grabs all associated cities
		values = starting_content.select('#areaAbb > option')

		# Storage for associated cities
		associated_cities = []

		if self.counter > 1:
			# Loops through associated cities and adds their HTML value to the list
			for city in values:
				associated_cities.append(city['value'])
				if city['value'] in self.visited:
					if city['value'] in self.queue:
						self.queue.remove('city')
					continue
				if city['value'] in self.queue:
					continue
				self.queue.append(city['value'])
			self.visited.append(starting_point)
			self.queue.remove(starting_point)
			# Add to the counter to keep track of iterations
			self.counter += 1
			self.sort_cities(self.queue[0])

		# If it is the first loop, add cities to both the queue and the associated cities
		elif self.counter == 1:
			for city in values:
				self.queue.append(city['value'])
				associated_cities.append(city['value'])
			self.visited.append('boston')
			self.queue.remove('boston')
			# Add to the counter to keep track of iterations
			self.counter += 1
			self.sort_cities(self.queue[0])
		else:
			print('Error with counter')

		print(self.complete_list)



crawler = Crawler()

# crawler.sort_cities('boston')
# crawler.gig_search('https://losangeles.craigslist.org/d/gigs/search/ggg', ['Church'], 3)
crawler.home_search('https://boston.craigslist.org/search/apa', 600, 900)

# Issue: Program was looping through each letter of the terms because I added it as a
# string and not an array.









