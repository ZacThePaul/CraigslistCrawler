import crawler as c
import json
import scraper as scraper
import database.Database as db

# if __name__ == '__main__':
# 	initiate_crawl = c.Crawler()


from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)


@app.route('/json')
def get_json():
	with open('data.json') as f:
		data = json.load(f)
		return data


@app.route('/get_listings')
def get_listings():
	keywords = request.args.get('keywords')
	category = request.args.get('category')
	days = request.args.get('days')
	crawl = c.Crawler(category, keywords, days)
	listings = vars(crawl)['complete_list']
	listings = json.dumps(listings)
	return listings


@app.route('/')
def hello_world():
	# crawl = c.Crawler()
	# gigs = crawl.sort_cities('boston')
	# print(vars(crawl))
	return render_template('home.html')


@app.route('/search')
def show_search():
	db.Database.build_db()
	return render_template('search.html')


if __name__ == '__main__':
	app.run()
