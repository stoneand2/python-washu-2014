# This reversal could be done within the larger hw5 file, as well

import csv

reversed_list = [] # blank array that reverse chronological csv will be read into, and then will read out into chronological csv

filename = "fare-deal-alert-2.csv"

readFile = open(filename, "rb")	
csvreader = csv.reader(readFile)

for row in csvreader:
	reversed_list.append(row)	# appends the csv row by row to the blank array
	
readFile.close()

header = reversed_list.pop(0)	# pop off headers (still want them at the top)

reversed_list.reverse()			# reverse the array items (each a full csv row) in place

reversed_list.insert(0, header)	# put the header back on top

newfile = open('chronological-fare-deals.csv', "wb")	# write to new csv file in chronological order
csvwriter = csv.writer(newfile)
csvwriter.writerows(reversed_list)
newfile.close()

