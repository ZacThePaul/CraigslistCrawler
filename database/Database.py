import sqlite3
from sqlite3 import Error


class Database:
	def __init__(self):
		self.filename = 'scrape_db'
		self.build_db()

	def build_db(self):
		conn = self.create_db_connection()

		build_queries = {
			'listings': '''CREATE TABLE IF NOT EXISTS listings (
							id integer PRIMARY KEY,
							title text NOT NULL,
							date text NOT NULL,
							type text NOT NULL
						);''',
		}

		# If more tables are needed, you can iterate through build_queries and run the function each time
		self.create_db_table(conn, build_queries['listings'])

		self.close_db_connection(conn)

	def create_db_connection(self):
		conn = None
		# Returns connection if valid
		try:
			conn = sqlite3.connect(self.filename)
			return conn
		# If invalid prints error
		except Error as e:
			print(e)

		return conn

	def close_db_connection(self, connection):
		connection.close()

	def create_db_table(self, connection, sql):
		try:
			c = connection.cursor()
			c.execute(sql)
		except Error as e:
			print(e)


