#Ricardo Granados
#A program than can calculate colories lose
# I will start by asking the name of the user> First and last name.
fullName = str (input("Hello there, what is your name?  "))

fName = (fullName[0:fullName.index(" ")])

sName = (fullName[fullName.index(" ")+1:])

print("So, your first name is ", fName)
print("and your second name is ", sName)
answer = input("Is this correct: " )
if answer == "Yes" or answer == "yes":
    print("Great, lets get started!")
elif answer == "No" or answer == "no":
    print ("Answer your name again")

#Next the program would calculate your body mass index
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))


calculate_body_mass_index = weight/(height/100)**2
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
# The countdown function is defined below

