#Akinola Daramola Jr
#Programming Exercise 4.2
#Due Date: 06/26/2022



"""
Calories Burned
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
"""

#Declaring value of calorie rate
calorie_rate = 4.2

#Declaring value of minutes
minutes = [10,15,20,25,30]

#Displaying calorie rate per minute
print(f"Calories burned per minute: {calorie_rate}")

#For loop
for calories in minutes:
    calorie_total = calories * calorie_rate     #Calculating calorie total
    print(f"Calories burned after {calories} minutes: {calorie_total:.2f}") #Display number on calories burned over time
