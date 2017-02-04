'''
Write the following function called print_numbers that has one interger 
input parameter called number and print the numbers from 1 up until number except
if the number is even and divisible by 3 print "penguin" instead.

Example
>>> print_numbers(13)

12345 "Pengin"7891011 "Penguin" 13

>>>print_numbers(4)

1 2 3 4

When you're finished push to the wrmup folder on your git-hub repository
'''

def print_numbers(number):
	for num in range(1,number +1):
		if num % 2 == 0 and num % 3 == 0:
			print ("Penguin") #Remember to qualify as a string using "" marks
		else:
			print (num)

print_numbers(13) # remember when calling the function to assure the call matches the function. 



 


