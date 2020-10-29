import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta, date
import json
import os
import urllib


class Crawler:

	def __init__(self, category, keywords, days):
		self.visited = []
		self.queue = []
		self.counter = 1
		self.cats = category
		self.keywords = keywords
		self.days = int(days)
		self.pages = {1: '?', 2: '?s=120', 3: '?s=240'}
		self.complete_list = {}
		self.sort_cities('boston')

	def gig_search(self, intended_url, terms, days=None):

		start = time.process_time()

		# Do this for each term the user wants found
		for single_term in terms:

			# If user chooses listings from today, append to url
			new_url = intended_url + '?query=' + single_term + '&is_paid=yes'

			print('new url = ', new_url)

			# Grab the content from the desired URL
			var = BeautifulSoup(requests.get(new_url).content, 'html.parser')

			things = var.findAll("p", {"class": "result-info"})

			for thing in things:
				datey = thing.find("time", {"class": "result-date"})
				listey = thing.find("a", {"class": "result-title"})
				datetime_object = datetime.strptime(datey['datetime'], '%Y-%m-%d  %H:%M')
				today = datetime.today()
				if days:
					# If the user specifies the range of days, compare the dates
					last_thurs = today - timedelta(days)
					if datetime_object > last_thurs:
						self.complete_list[listey.text] = listey['href']
						listinos = {listey.text: listey['href']}

						if os.stat("data.json").st_size == 0:
							with open('data.json', 'w') as f:
								json.dump(listinos, f, ensure_ascii=False)
						else:
							with open('data.json') as f:
								data = json.load(f)
								data.update(listinos)
								with open('data.json', 'w') as f:
									json.dump(data, f, ensure_ascii=False)

				else:
					# If the user does not specify the range of days, no need to compare, just give them everything
					self.complete_list[listey.text] = listey['href']

	# Find all links with the CSS class of "result-title"
			# titles = var.findAll("a", {"class": "result-title"})
			#
			# dates = var.findAll("time", {"class": "result-date"})

			# for single_date in dates:
			# 	# This is how we see which date is after which
			# 	datetime_object = datetime.strptime(date['datetime'], '%Y-%m-%d  %H:%M')
			# 	today = datetime.today()
			# 	last_thurs = today - timedelta(5)
			# 	dt2 = datetime.strptime('2020-11-19 16:01', '%Y-%m-%d  %H:%M')
			#
			# 	if datetime_object > last_thurs:
			# 		print('datetime object is greater than')

			# test = var.select('p.result-info > .result-date')

			# for res in test:
			# 	print(res['datetime'])

			# For each listing that is shown, add to complete_list
			# for listing in titles:
			# 	self.complete_list[listing.text] = (listing['href'])

		# print('Gig Search took: ', time.process_time() - start)

	def home_search(self, intended_url, min_price, max_price):

		lister = {}

		new_url = intended_url + '?min_price=' + str(min_price) + '&max_price=' + str(max_price)

		soup = BeautifulSoup(requests.get(new_url).content, 'html.parser')

		titles = soup.findAll("a", {"class": "result-title"})

		for title in titles:
			# return "<a href='" + title['href'] + "'>" + title.text + "</a>"
			lister[title.text] = title['href']
			# print(title.text + ' : ' + title['href'])
		return lister

	def sort_cities(self, starting_point):

		# start = time.process_time()

		print(self.counter, ' cities crawled.')

		if self.counter == 50:
			listings = self.complete_list
			print(listings)

		# If there has been more than two loops through and the queue is empty, something is broken.
		if self.counter > 2 and len(self.queue) < 2:
			listings = self.complete_list
			return listings

		if self.cats == 'job':
			starting_url = 'https://' + starting_point + '.craigslist.org/search/jjj'
		if self.cats == 'gig':
			starting_url = 'https://' + starting_point + '.craigslist.org/search/ggg'

		dirty_terms = self.keywords.split('-')

		# Grab the content!
		self.gig_search(starting_url, dirty_terms, self.days)

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
						# print('City sort took: ', time.process_time() - start)
					continue
				if city['value'] in self.queue:
					# print('City sort took: ', time.process_time() - start)
					continue
				self.queue.append(city['value'])

			self.visited.append(starting_point)
			self.queue.remove(starting_point)

			# Add to the counter to keep track of iterations
			self.counter += 1
			# print('City sort took: ', time.process_time() - start)
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
