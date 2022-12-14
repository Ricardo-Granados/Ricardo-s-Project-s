#Ricardo Granados
#This program will calculate your body mass index and it will tell you if your overweight or not
# I will start by asking the name of the user> First and last name.
fullName = str (input("Hello there, what is your full name? "))

first_Name = (fullName[0:fullName.index(" ")])

last_Name = (fullName[fullName.index(" ")+1:])

print("So, your first name is ", first_Name)
print("and your second name is ", last_Name)
answer = input("Is this correct: " )
if answer == "Yes" or answer == "yes":
    print("Great, lets get started!")
elif answer == "No" or answer == "no":
    print ("Answer your name again")

#Next the program would calculate your body mass index
#I choose the metric system because is much more easie than the emperial system
height = float(input("Enter your height in cm: "))
if height < 0:
    print ("Please enter your height")

weight = float(input("Enter your weight in kg: "))
if weight < 0:
    print ("Please answer your weight in kg")


calculate_body_mass_index = weight/(height//100)**2
print ("Your Body mas Index is: ", calculate_body_mass_index)
# A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9.
if calculate_body_mass_index >= 25.0:
    print ("The results indicate that your are overweight")
elif calculate_body_mass_index > 18.9 :
    print ("You are on the healthy range")
elif calculate_body_mass_index < 18.9:
    print ("You are slightly unhealthy")

    
#Now the program will calculate how many calories you burned in total
    
time = int(input('How many minutes were you exercising? '))
calories = 0  
for i in range(time):
    calories += 3.4

print('According to your body mass index your burned {} calories'.format(calories))
# Now the program will choose a random exercise you can do
#This willbe fun activity
import random

item_list = ["Pushups", "Pullups","Squats"]
number_list = [1,20]
# random exercise from list
print("Randomly I choose one exercise for you. Do", random.choice(number_list), random.choice(item_list))

response = input("Once completed, submit Done ", )
if response == "done" or response == "Done":
    print("Great, lets continue")
