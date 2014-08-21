import tweepy
import time
import csv
import datetime

auth = tweepy.OAuthHandler('###API key here###', '###API secret here###')
auth.set_access_token('### Access token here###', '###Access token secret here###')    
api = tweepy.API(auth)

api.rate_limit_status()

# Task 1: The most_followers() function will determine the follower of the target user with the most followers

def most_followers():
	my_friend = api.get_user('adoxner')			# Get target user
	print my_friend
	
	array = []	
	filename = "1st_degree_most_followers_1.csv"	# A csv that will have follower, follower_count pairs written to it
	headers = ["User", "Number of Followers"]
	
	most_followers = 0 							# Baseline of 0 followers. Loop through all followers of my_friend. If any one of them has more than 0 followers , override with their # and keep looping. Repeat for all followers 
	counter = 0 								# Counts which follower of my_friend you are on until all are through

	friend_followers = api.followers_ids(id=my_friend.screen_name)	# List of followers of my_friend
	
	while counter < len(friend_followers): 							# As long as haven't checked all followers
		try:														# Try, because there can be exceptions raised
			follower = api.get_user(friend_followers[counter])		# Get the follower's user id
			array.append([str(follower.screen_name), follower.followers_count])	# Array to be entered as a row in csv
			
			readFile = open(filename, "wb")							# Add the follower and their count to the csv for later usage
			csvwriter = csv.writer(readFile)
			csvwriter.writerow(headers)
			csvwriter.writerows(array)
			readFile.close()
			
			if follower.followers_count > most_followers:					# If the follower's follower count is more than the previous highest
				most_followers = follower.followers_count					# Set the new highest to be their number
				the_user_with_most_followers = str(follower.screen_name)	# And the user w/ the most to be them
			counter += 1													# Loop on to the next follower
		except tweepy.TweepError: 											# If get an error from tweepy (timed out), sleep and try again. Lets you keep going w/o ending function
			time.sleep(.20)

	print "The follower with the most followers is:", the_user_with_most_followers # Metric, 216K followers. Can be verified in the csv file!


# Task 4: The most_active() function determines most active of those my target user follows
# Activity defined as tweets per day, over the entire lifespan of the user's account

def most_active():
	my_friend = api.get_user('adoxner')							# Get target user
	
	who_he_follows = api.friends_ids(id=my_friend.screen_name)	# Get list of who target user follows
	
	top_ratio = 0												# The current highest tweets/day ratio
	counter = 0													# Counts which user you are on
	
	array = []
	filename = "active_followers.csv"							# csv to write to
	headers = ["User", "Tweets per Day"]
	
	while counter < len(who_he_follows):						# As long as haven't looped through all of those who target user follows
		try:
			today = datetime.datetime(2014, 8, 20)				# Today's date
			today_date = today.date()
			follower = api.get_user(who_he_follows[counter])	# Obtain the user id
			follower_total_tweets = follower.statuses_count		# Obtain their total number of tweets
			follower_created_date = follower.created_at.date()	# Obtain the date of their account's creation
			time_since_creation = today_date - follower_created_date	# Obtain days from today to their account creation
			days_since_creation = time_since_creation.days
			tweet_day_ratio = float(follower_total_tweets) / float(days_since_creation)	# Calculate ratio, using floating point
			array.append([str(follower.screen_name), tweet_day_ratio])	# Will be written to csv
			
			readFile = open(filename, "wb")						# Writing to the csv
			csvwriter = csv.writer(readFile)
			csvwriter.writerow(headers)
			csvwriter.writerows(array)
			readFile.close()		
			
			if tweet_day_ratio > top_ratio:						# If the user has the highest ratio thus far
				top_ratio = tweet_day_ratio						# Make the top ratio their ratio
				most_active_user = str(follower.screen_name)	# Make them the most active user
			counter += 1										# Move on to the next follower
		except tweepy.TweepError:
			time.sleep(.20)
	print "The most active user is:", most_active_user # SCsupport, 47.19617622610 tweets per day. Can be verified in the csv file!
	print "Their tweet to days on twitter ratio is:", top_ratio, "tweets per day."	
			
			
			
	