def is_triangle(int1, int2, int3):
	print int1
	print int2
	print int3
	
	if int1 + int2 <= int3:
		print "No."
	elif int2 + int3 <= int1:
		print "No."
	elif int1 + int3 <= int2:
		print "No." 
	else:
		print "Yes."

is_triangle(1, 2, 3)

def input_lengths():
	length1 = int(raw_input("Input the length of stick one: "))
	length2 = int(raw_input("Input the length of stick two: "))
	length3 = int(raw_input("Input the length of stick three: "))
	
	print length1
	print length2
	print length3
	
	if length1 + length2 <= length3:
		print "No."
	elif length2 + length3 <= length1:
		print "No."
	elif length1 + length3 <= length2:
		print "No." 
	else:
		print "Yes."
		
input_lengths()
	