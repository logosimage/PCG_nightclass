'''
Portland Code Guild; Full Stack Python Developer Boot Camp.
Evening Class from 6 pm to 9:30pm.Begining January 17  2017 through May 9th 2017
Instructor:  Matthew Hemmingsen
Today's Date:
Today's Lesson Subject(s):
'''
'''
mjhemmingsen [6:18 PM]
Write four separate functions one called add, one called subtract, one called multiply,
and one called divide. Each function will take 2 input arguments that are integers.
Instead of printing the answer instead use the return keyword to return the answer
(this will not print it) example for the add method instead of using
print(x + y)do this return x + y
at the end of your function than to test your function out just call it inside a print statement for example
print(add(3,5)) this will then print 8 to the user.

MAKE SURE YOU HAVE NO PRINT STATEMENTS IN YOUR FUNCTION BODY
THIS WILL THROW ERRORS WHEN RUNNING!!!
'''

def add (a, b):
    return 'answer is', a+ b
print (add (5, 6))


def subtract (num1, num2):
    return "answer is", num1 - num2
print (subtract (10,6))


def multiply (num1, num2):
    return ("answer is", num1 * num2)
print (multiply (20, 4))


def divide (number1, num2):
    return ("answer is", number1 / num2)
print (divide(20,4))
'''
#git add file/ filename
# git commit - "for.py"
# git push
'''