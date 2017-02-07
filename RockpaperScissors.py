#RockpaperScissors

# two user inputed numbers and print which user enter the highest number
'''
user_one = int(input("Enter a number user one"))

user_two = int(input("Enter a number user two"))

sentence = "{} had a greater number the number was {} "
# first case user_one's number is greater
if user_one > user_two:
   print(sentence.format("User One", user_one))
   
# second case user_two's number is greater

elif user_two > user_one:
   
   print(sentence.format("User two", user_two))
   
# third they are the same
else:
   
   print("You entered the same number")'''
   

   
   


user_one = input("User one, Enter rock, paper or scissors")

user_two = input("User two, Enter rock, paper or scissors")

# check if user_one entered rock and user_two entered scissoers
if user_one == "rock" and user_two == "scissors":
#print user_one wins
	print ("user one wins")
elif user_one == "paper" and user_two == "scissors":
    print ("user two wins")
elif user_one == "scissors" and user_two == "paper":
	print ("user one wins")
elif user_one == "scissors" and user_two == "rock":
	print ("user two wins")
elif user_one == "paper" and user_two == "rock":
	print ("user one wins")
elif user_one == "rock" and user_two == "paper":
	print ("user_one wins")

else:
	print ("It's a tie")
	#elif


# Which direction to go Notes:'''