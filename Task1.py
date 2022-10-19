#Author: Roy Afaryan 
#Assignment: Project 1
#Completed 9/19/2022

import math

#Task 1

#function to calculate English system BMI
def English(lb, inch):
    BMI = 703*lb/(inch**2)
    return BMI

#function to calculate Metric system BMI
def Metric(kg, meter):
    BMI = kg/(meter**2)
    return BMI

#while loop that ensures user puts valid inputs
correct = 1
while correct:
    systemType = str(input("Please enter 'Metric' or 'English' to determine which system you would like to use to calculate BMI: "))
    if systemType == "Metric" or systemType == "metric" or systemType == "English" or systemType == "english":
        correct -= 1 #exit while
    else:
        print("Please try again.")
        continue

#Metric BMI calculator
if systemType == "Metric" or systemType == "metric": #checks condition
    correct = 1
    while correct:
        try:
            metricWeight = float(input("Please enter weight in kilograms: "))
            metricHeight = float(input("Please enter height in meters: "))
        except(ValueError): #exception handler in case float is not inputted
            print("Please enter float.\n")
            continue

        if metricWeight <= 0 or metricHeight <= 0: #ensures user enters non-zero values
            print("Please enter valid height and weight.\n")
            continue
        else:
            metricBMI = Metric(metricWeight, metricHeight)
            roundedBMI = round(metricBMI, 1)

            print("Your BMI is", roundedBMI)
            if metricBMI < 18:
                print("You are underweight.")
            elif metricBMI > 25:
                print("You are overweight.")
            else:
                print("You have a healthy BMI.")
            correct -= 1 #exit while

#English BMI calculator
if systemType == "English" or systemType == "english": #checks condition
    correct = 1
    while correct:
        try:
            englishWeight = float(input("Please enter weight in pounds: "))
            englishHeight = float(input("Please enter height in inches: "))
        except(ValueError): #exception handler in case float is not inputted
            print("Please enter float.\n")
            continue

        if englishWeight <= 0 or englishHeight <= 0: #ensures user enters non-zero values
            print("Please enter valid height and weight.\n")
            continue
        else:
            englishBMI = English(englishWeight, englishHeight)
            roundedBMI = round(englishBMI, 1)

            print("Your BMI is", roundedBMI)
            if englishBMI < 18:
                print("You are underweight.")
            elif englishBMI > 25:
                print("You are overweight.")
            else:
                print("You have a healthy BMI.")
            correct -= 1 #exit while
'''
Test Run #1
Please enter 'Metric' or 'English' to determine which system you would like to use to calculate BMI: english
Please enter weight in pounds: 150
Please enter height in inches: 72
Your BMI is 20.3
You have a healthy BMI.

Test Run #2
Please enter 'Metric' or 'English' to determine which system you would like to use to calculate BMI: English
Please enter weight in pounds: 175
Please enter height in inches: 68
Your BMI is 26.6
You are overweight.

Test Run #3
Please enter 'Metric' or 'English' to determine which system you would like to use to calculate BMI: metric
Please enter weight in kilograms: 72
Please enter height in meters: 1.83
Your BMI is 21.5
You have a healthy BMI.

Test Run #4
Please enter 'Metric' or 'English' to determine which system you would like to use to calculate BMI: Metric
Please enter weight in kilograms: 50.5
Please enter height in meters: 1.68
Your BMI is 17.9
You are underweight.

Test Run #5
Please enter 'Metric' or 'English' to determine which system you would like to use to calculate BMI: english
Please enter weight in pounds: 135
Please enter height in inches: 67
Your BMI is 21.1
You have a healthy BMI.

Test Run #6
Please enter 'Metric' or 'English' to determine which system you would like to use to calculate BMI: English
Please enter weight in pounds: 160
Please enter height in inches: 70
Your BMI is 23.0
You have a healthy BMI.

Test Run #7
Please enter 'Metric' or 'English' to determine which system you would like to use to calculate BMI: metric
Please enter weight in kilograms: 100
Please enter height in meters: 1.7
Your BMI is 34.6
You are overweight.

Test Run #8
Please enter 'Metric' or 'English' to determine which system you would like to use to calculate BMI: Metric
Please enter weight in kilograms: 75
Please enter height in meters: 1.2
Your BMI is 52.1
You are overweight.

Test Run #9
Please enter 'Metric' or 'English' to determine which system you would like to use to calculate BMI: English
Please enter weight in pounds: tjfdalkji
Please enter float.

Please enter weight in pounds: 80
Please enter height in inches: jfdainfda
Please enter float.

Please enter weight in pounds: 120
Please enter height in inches: 0
Please enter valid height and weight.

Please enter weight in pounds: 140  
Please enter height in inches: 65
Your BMI is 23.3
You have a healthy BMI.

Test Run #10
Please enter 'Metric' or 'English' to determine which system you would like to use to calculate BMI: metric
Please enter weight in kilograms: fsa
Please enter float.

Please enter weight in kilograms: 60
Please enter height in meters: fsa
Please enter float.

Please enter weight in kilograms: 60
Please enter height in meters: 0
Please enter valid height and weight.

Please enter weight in kilograms: 60
Please enter height in meters: 1.3
Your BMI is 35.5
You are overweight.
'''