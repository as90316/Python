#Ask user for Name
name = input('Enter your name :-> ')
#Ask user for Age
age = input ('Enter your Age:-> ') # input function always turns into integer
age = int(age) + 1

#Ask user for City
city = input ('Enter the city where you live:- ')

#Ask user what they enjoy

hobby = input ('What is your hobby:-> ')

print ('My Name is ',name, '. I am ',str(age),' years old', '\n', '. I stay in ',city, ' and I enjoy', hobby )

# Lets format it nicely using format function

final_message = "My Name is {}. I am {} years old. \n  I stay in {} city. I like {}".format(name,age,city,hobby)

print (final_message)

#Let us Shuffle
final_message = "My Name is {3}. I am {1} years old. \n  I stay in {2} city. I like {0}".format(name,age,city,hobby)

print (final_message)

print (final_message.count('a'))
