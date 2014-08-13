import random

random_list = random.sample(xrange(1000000), 10000) # generates list of 10000 random numbers w/0 replacement from range 1000000

# merge sort implementation draws from pseudocode written on 8/7/14 in class
# merge sort is O(n log n) in the worst case

def merge_sort(list):
	
	if len(list) <= 1: return list	#base case--if the list has 0-1 items, it's already sorted!
	
	left_half = merge_sort(list[:len(list)/2])	# recursively splits original list in half
	right_half = merge_sort(list[len(list)/2:])
	
	return re_merge(left_half, right_half)	# calls the function that will merge lists back together
	
def re_merge(left_half, right_half):
	sorted_list = []	# the list in sorted form
	
	while len(left_half) > 0 or len(right_half) > 0:	# ensures re_merge while loop occurs until both split lists are fully sorted into the new list
		if len(left_half) > 0 and len(right_half) > 0:	# case where both halves still have items in them
			if left_half[0] > right_half[0]:	# if the first item of the left is greater than the first item of right, put the right onto the sorted list, take it off the right list and loop the function over again 
				sorted_list.append(right_half[0])
				right_half.pop(0)
			else:
				sorted_list.append(left_half[0])
				left_half.pop(0)
		elif len(right_half) > 0:	# the case where only the right half has elements
			sorted_list.append(right_half[0])
			right_half.pop(0)
		elif len(left_half) > 0:	# the case where only the left half has elements
			sorted_list.append(left_half[0])
			left_half.pop(0)		
	return sorted_list	# after while loop finishes, returns the sorted list

# selection sort implementation draws from pseudocode written on 8/7/14 in class, as well as code written for merge sort
# selection sort is O(n**2) in the worst case

def selection_sort(list):

	if len(list) <= 1: return list	#base case--if the list has 0-1 items, it's already sorted!
	
	new_sorted_list = []	# list to sort into
	
	position = 0
	while len(list) > 0: 	# as long as there are still items in the unsorted list
		if len(new_sorted_list) > position:		
			if list[0] > new_sorted_list[position]:	# if first item in unsorted list is greater than x item in the sorted list, check again w/ next item in sorted list
				position += 1
			else:
				new_sorted_list.insert(position, list[0]) # first time number is greater than x item in sorted list, so insert it behind that number
				list.pop(0)	# take it off unsorted list
				position = 0	# do it again w/ new list[0]
		else:	# this is the case when the number is greater than all in the sorted list, so can just append to end of sorted
			new_sorted_list.append(list[0])
			list.pop(0)
			position = 0
	return new_sorted_list

# BONUS
# quick_sort algorithm adapted from: https://stackoverflow.com/questions/18262306/quick-sort-with-python

def quick_sort(list):
	less_than_pivot = []
	equal_to_pivot = [] # will be empty if using random.sample as it is w/o replacement
	more_than_pivot = []

	if len(list) <= 1: return list	# base case where list is already sorted 
	
	pivot_choice = list[0] 	# picking "pivot". wikipedia notes speed problems w/ choosing 1st element if list is close to reverse sorted
							# list is random, so this is okay
	for number in list:
		if number > pivot_choice:	# if more than pivot, add it to the more_than list
			more_than_pivot.append(number)
		elif number == pivot_choice:
			equal_to_pivot.append(number)
		else:
			less_than_pivot.append(number)
	return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(more_than_pivot)	# recursive until all are into more/less/equal. then re-combine into newly sorted list

# print merge_sort(random_list)
# print quick_sort(random_list)		
# print selection_sort(random_list)
		
		
		
		
	