# The blog I used does have a comments section, but no comments have been made (Matt said this was okay)
# The blog has no specified authors (Matt said this was okay)

from bs4 import BeautifulSoup
import csv 
from nltk.util import clean_html
import urllib2 
import time
import sys

page_to_scrape = 'http://faredealalert.com/'	# The main homepage. Allows scraper to always start at the first post

headers = ["Boolean", "Title", "Date", "URL"]	# Info wanted, will be headers on the CSV file

filename = "fare-deal-alert-2.csv"			# CSV file to save info

webpage = urllib2.urlopen(page_to_scrape)	# Open homepage

soup = BeautifulSoup(webpage.read())		# Parse homepage
soup.prettify()		
	
flight_deals = soup.findAll("a", attrs={'rel':'bookmark'})	# Find first post from the homepage
first_deal = flight_deals[0]
new_url = first_deal.get('href')
print new_url

webpage = urllib2.urlopen(new_url)		# Open the first post page
soup = BeautifulSoup(webpage.read())
soup.prettify()

url_div = soup.find("div", attrs={'class':'prev_next'})
previous_checker = clean_html(str(url_div.find("p")))

flights_array = []		# Array used to store info from each post before putting into CSV file

while "Previous post" in previous_checker:		# Each post's html links to "previous post", except the final one
												# So, while loop continues until the final post on the blog
	post_page = urllib2.urlopen(new_url)		# Open the webpage with the blog post

	soup = BeautifulSoup(post_page.read())		# Parse the webpage
	soup.prettify()
	
	title_of_deal = soup.find("title")			# Extract title of deal on page
	clean_title = clean_html(str(title_of_deal))

	date_deal_posted = soup.find("p", attrs={'class':'headline_meta'})	# Extract date of deal post
	clean_date = clean_html(str(date_deal_posted))

	is_it_a_page = soup.find("div", attrs={'class':'prev_next'})	# Boolean to test if page is post or not
	the_determinant = clean_html(str(is_it_a_page.find("p")))		# Check if there is a "post" in the prev_next html class (from homepage to second page has a prev_next class, but doesn't have the post keyword)
	if "post" in the_determinant:
		boolean = 1
	else:
		boolean = 0
	
	next_url_div = soup.find("div", attrs={'class':'prev_next'})		# Find the next URL to re-loop with
	previous_checker = clean_html(str(next_url_div.find("p")))			# Checks if there is a previous post
	
	flights_array.append([boolean, clean_title, clean_date, new_url])	# Add this post's info to the array
	
	next_url_a = next_url_div.find("a")
	new_url = next_url_a.get('href')		# Gets the next post's URL

	time.sleep(.125)						# Sleeps for .125 seconds
	
	readFile = open(filename, "wb")			# Add the post's info to the CSV
	csvwriter = csv.writer(readFile)
	csvwriter.writerow(headers)
	csvwriter.writerows(flights_array)
	readFile.close()

	