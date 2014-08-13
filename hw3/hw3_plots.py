import unittest
import random
import hw3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def merge_sort(n_to_sort):
	hw3.merge_sort(random.sample(xrange(1000000), n_to_sort))
def selection_sort(n_to_sort):
	hw3.selection_sort(random.sample(xrange(1000000), n_to_sort))
def quick_sort(n_to_sort):
	hw3.quick_sort(random.sample(xrange(1000000), n_to_sort))

if __name__ == '__main__':
	import timeit
	merge_sort_time_1000 = (timeit.timeit("merge_sort(1000)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_2500 = (timeit.timeit("merge_sort(2500)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_5000 = (timeit.timeit("merge_sort(5000)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_7500 = (timeit.timeit("merge_sort(7500)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_10000 = (timeit.timeit("merge_sort(10000)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_12500 = (timeit.timeit("merge_sort(12500)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_15000 = (timeit.timeit("merge_sort(15000)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_17500 = (timeit.timeit("merge_sort(17500)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_20000 = (timeit.timeit("merge_sort(20000)", setup="from __main__ import merge_sort", number=1))
	
	merge_list = [merge_sort_time_1000, merge_sort_time_2500, merge_sort_time_5000, merge_sort_time_7500,
	merge_sort_time_10000, merge_sort_time_12500, merge_sort_time_15000, merge_sort_time_17500, merge_sort_time_20000]
	print merge_list
	
	selection_sort_time_1000 = (timeit.timeit("selection_sort(1000)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_2500 = (timeit.timeit("selection_sort(2500)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_5000 = (timeit.timeit("selection_sort(5000)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_7500 = (timeit.timeit("selection_sort(7500)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_10000 = (timeit.timeit("selection_sort(10000)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_12500 = (timeit.timeit("selection_sort(12500)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_15000 = (timeit.timeit("selection_sort(15000)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_17500 = (timeit.timeit("selection_sort(17500)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_20000 = (timeit.timeit("selection_sort(20000)", setup="from __main__ import selection_sort", number=1))
	
	selection_list = [selection_sort_time_1000, selection_sort_time_2500, selection_sort_time_5000, selection_sort_time_7500, 
	selection_sort_time_10000, selection_sort_time_12500, selection_sort_time_15000, selection_sort_time_17500, selection_sort_time_20000]
	print selection_list

	quick_sort_time_1000 = (timeit.timeit("quick_sort(1000)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_2500 = (timeit.timeit("quick_sort(2500)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_5000 = (timeit.timeit("quick_sort(5000)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_7500 = (timeit.timeit("quick_sort(7500)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_10000 = (timeit.timeit("quick_sort(10000)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_12500 = (timeit.timeit("quick_sort(12500)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_15000 = (timeit.timeit("quick_sort(15000)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_17500 = (timeit.timeit("quick_sort(17500)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_20000 = (timeit.timeit("quick_sort(20000)", setup="from __main__ import quick_sort", number=1))
	
	quick_sort_list = [quick_sort_time_1000, quick_sort_time_2500, quick_sort_time_5000, quick_sort_time_7500, 
	quick_sort_time_10000, quick_sort_time_12500, quick_sort_time_15000, quick_sort_time_17500, quick_sort_time_20000]
	print quick_sort_list

	merge_sort_time_100 = (timeit.timeit("merge_sort(100)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_200 = (timeit.timeit("merge_sort(200)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_300 = (timeit.timeit("merge_sort(300)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_400 = (timeit.timeit("merge_sort(400)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_500 = (timeit.timeit("merge_sort(500)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_600 = (timeit.timeit("merge_sort(600)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_700 = (timeit.timeit("merge_sort(700)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_800 = (timeit.timeit("merge_sort(800)", setup="from __main__ import merge_sort", number=1))
	merge_sort_time_900 = (timeit.timeit("merge_sort(900)", setup="from __main__ import merge_sort", number=1))
	
	merge_list_2 = [merge_sort_time_100, merge_sort_time_200, merge_sort_time_300, merge_sort_time_400,
	merge_sort_time_500, merge_sort_time_600, merge_sort_time_700, merge_sort_time_800, merge_sort_time_900]
	print merge_list_2
	
	selection_sort_time_100 = (timeit.timeit("selection_sort(100)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_200 = (timeit.timeit("selection_sort(200)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_300 = (timeit.timeit("selection_sort(300)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_400 = (timeit.timeit("selection_sort(400)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_500 = (timeit.timeit("selection_sort(500)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_600 = (timeit.timeit("selection_sort(600)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_700 = (timeit.timeit("selection_sort(700)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_800 = (timeit.timeit("selection_sort(800)", setup="from __main__ import selection_sort", number=1))
	selection_sort_time_900 = (timeit.timeit("selection_sort(900)", setup="from __main__ import selection_sort", number=1))
	
	selection_list_2 = [selection_sort_time_100, selection_sort_time_200, selection_sort_time_300, selection_sort_time_400, 
	selection_sort_time_500, selection_sort_time_600, selection_sort_time_700, selection_sort_time_800, selection_sort_time_900]
	print selection_list_2

	quick_sort_time_100 = (timeit.timeit("quick_sort(100)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_200 = (timeit.timeit("quick_sort(200)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_300 = (timeit.timeit("quick_sort(300)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_400 = (timeit.timeit("quick_sort(400)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_500 = (timeit.timeit("quick_sort(500)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_600 = (timeit.timeit("quick_sort(600)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_700 = (timeit.timeit("quick_sort(700)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_800 = (timeit.timeit("quick_sort(800)", setup="from __main__ import quick_sort", number=1))
	quick_sort_time_900 = (timeit.timeit("quick_sort(900)", setup="from __main__ import quick_sort", number=1))

	quick_sort_list_2 = [quick_sort_time_100, quick_sort_time_200, quick_sort_time_300, quick_sort_time_400, 
	quick_sort_time_500, quick_sort_time_600, quick_sort_time_700, quick_sort_time_800, quick_sort_time_900]
	print quick_sort_list_2

n_list = [1000, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]
n_list_2 = [100, 200, 300, 400, 500, 600, 700, 800, 900]


pp = PdfPages('hw3_plots_1.pdf')
plt.plot(n_list, merge_list, 'ro-', label='merge sort')
plt.plot(n_list, selection_list, 'bo-', label='selection sort')
plt.plot(n_list, quick_sort_list, 'go-', label='quick sort')
plt.title('Plot 1: Sorting Time for a Large N List by Algorithm')
plt.xlabel('Size of List to Sort (N)')
plt.ylabel('Time Taken to Sort (seconds)')
plt.legend(loc='upper left')
pp.savefig()
plt.close()

plt.plot(n_list_2, merge_list_2, 'ro-', label='merge sort')
plt.plot(n_list_2, selection_list_2, 'bo-', label='selection sort')
plt.plot(n_list_2, quick_sort_list_2, 'go-', label='quick sort')
plt.title('Plot 2: Sorting Time for a Small N List by Algorithm')
plt.xlabel('Size of List to Sort (N)')
plt.ylabel('Time Taken to Sort (seconds)')
plt.legend(loc='upper left')
pp.savefig()
plt.close()
pp.close()
	
