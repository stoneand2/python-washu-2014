import sqlalchemy
import csv

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)	# Can also set up in local database
Base = declarative_base()

### HW 5 ###
### To run in the Python interpreter, I've copied & pasted each class one at a time ###

class BlogPost(Base):				# Class for instances of each blog post from HW5 
	__tablename__ = 'scrapes'
	
	id = Column(Integer, primary_key = True)
	title = Column(String)
	date = Column(String)
	url = Column(String)
	connection = Column(Integer, ForeignKey('source.id'))	# Allows connecting all the posts to the same source website
	
	def __init__(self, title, date, url):
		self.title = title
		self.date = date
		self.url = url
	
	def __repr__(self):		# If printing, this is what will be displayed
		return "<BlogPost(title='%s',date='%s')>" % (self.title, self.date)

class Source(Base):		# The class for the source website's URL and title
	__tablename__ = 'source'
	
	id = Column(Integer, primary_key = True)
	source_url = Column(String, nullable = False)
	name = Column(String, nullable = False)
	
	def __init__(self, source_url, name):
		self.source_url = source_url
		self.name = name
	
	blogpost = relationship("BlogPost", backref=backref('source', order_by = id))	# Relates this back to the post class

Base.metadata.create_all(engine)		# Create the tables
Session = sessionmaker(bind=engine)		# Create a session to interact with the database
session = Session()

main_source = Source('faredealalert.com', 'The Fare Deal Alert')	# Instance of the source website class
session.add(main_source)
session.commit()

def hw5_to_database():
	filename = "fare-deal-alert-2.csv"		# The file with all of the blog post information
	
	readFile = open(filename, "rb")
	csvreader = csv.reader(readFile)
	
	for row in csvreader:				# For every post in the CSV file
		boolean = row.pop(0)			
		post_title = row.pop(0)
		post_date = row.pop(0)
		post_url = row.pop(0)
		
		post = BlogPost(title = post_title, date = post_date, url = post_url)	# Creates an instance of the BlogPost class
		main_source.blogpost.append(post)		# Ties every post to the same source website
		session.add(post)
		session.commit()
	
	readFile.close()

hw5_to_database()

### HW6 ###
### To run, I've copied + pasted each class below into the Python interpreter one at a time ###
### If running separate from the HW5 part above, must also enter lines 1-10 and 168-170 ###

class User(Base):		# User class, to create an instance of your target user
	__tablename__ = 'target_user'
	
	id = Column(Integer, primary_key = True)
	username = Column(String, nullable = False)
	
	follow_user = relationship("FollowUser", backref=backref('target_user', order_by = id))	# Relationship to those who follow the target user
	user_follows = relationship("UserFollows", backref=backref('target_user', order_by = id))	# Relationship to those who user follows
	crawling = relationship("Crawls", backref=backref('target_user', order_by = id))	# Relationship to a specific crawl
	
	def __init__(self, username):
		self.username = username
		
	def __repr__(self):
		return "<Target(username='%s')>" % (self.username)
		
class FollowUser(Base):	# Class used to create instances for every user that follows the target user
	__tablename__ = 'follow_user'
	
	id = Column(Integer, primary_key = True)
	username = Column(String, nullable = False)
	number_of_followers = Column(Integer, nullable = False)
	connect_to_target = Column(Integer, ForeignKey('target_user.id'))	# Connects the user to the target user's id
	
	def __init__(self, username, number_of_followers):
		self.username = username
		self.number_of_followers = number_of_followers
	def __repr__(self):
		return "<Target(username='%s', number_of_followers='%s'>)" % (self.username, self.number_of_followers)

class UserFollows(Base):	# Class used to create instances for every user that the target follows
	__tablename__ = 'user_follows'
	
	id = Column(Integer, primary_key = True)
	username = Column(String, nullable = False)
	tweets_per_day = Column(String, nullable = False)
	connect_to_target = Column(Integer, ForeignKey('target_user.id'))	# Connects the user to the target user's id
	
	def __init__(self, username, tweets_per_day):
		self.username = username
		self.tweets_per_day = tweets_per_day
	def __repr__(self):
		return "<Target(username='%s', tweets_per_day='%s'>)" % (self.username, self.tweets_per_day)
		
class Crawls(Base):	# Class to create an instance of a unique crawl
	__tablename__ = 'crawls'
	
	id = Column(Integer, primary_key = True)
	date_of_crawl = Column(String, nullable = False)
	crawled_starter_id = Column(Integer, ForeignKey('target_user.id'))	 # Ties to the target user's id
	
	def __init__(self, date_of_crawl):
		self.date_of_crawl = date_of_crawl
	def __repr__(self):
		return "<Cralws(date='%s')" % (self.date_of_crawl)

def hw6_part1_to_database():
	filename = "1st_degree_most_followers.csv"	# Opens file with all of the target user's followers
	
	readFile = open(filename, "rb")
	csvreader = csv.reader(readFile)
	
	for row in csvreader:
		name_of_user = row.pop(0)
		number_followers = row.pop(0)
		
		user_who_follows = FollowUser(name_of_user, number_followers)	# Create instance of a follower
		primary_target.follow_user.append(user_who_follows)	# Tie all of them to the same target user
		session.add(user_who_follows)
		session.commit()
		
	readFile.close()
	
def hw6_part4_to_database():
	filename = "active_followers.csv"	# Opens file with all of the users the target follows
	
	readFile = open(filename, "rb")
	csvreader = csv.reader(readFile)
	
	for row in csvreader:
		name_of_user = row.pop(0)
		tweets_per = row.pop(0)
		
		followed_user = UserFollows(name_of_user, tweets_per)	# Create instance of a user
		primary_target.user_follows.append(followed_user)	# Tie all of them to the same target user
		session.add(followed_user)
		session.commit()
	
	readFile.close()

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
	
primary_target = User('adoxner')	# Create instance of the target user
session.add(primary_target)
first_crawl = Crawls('August 21, 2014. 4:14 PM')	# Create instance of the unique crawl
session.add(first_crawl)
primary_target.crawling.append(first_crawl)	# Tie the unique crawl to the target user
session.commit()

hw6_part1_to_database()
hw6_part4_to_database()





