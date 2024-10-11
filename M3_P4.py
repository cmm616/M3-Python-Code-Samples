#Corinthian M
#Oct 8, 2024
#This program calculates the MPG (mialage per gallon) of a 2024 Jeep Renegade. 
def calculate_mpg():
#Jeep Renegade MPG values that I found on the internet.
    city_mpg = 24
    highway_mpg = 32
#Code to prompt the user for miles drivin in the city and drivin on the highway. i usedd the float command so users can imput boh options for a more tailored result.
    city_miles = float(input("Enter the number of miles driven in the city: "))
    highway_miles = float(input("Enter the number of miles driven on the highway: "))
#This string of code calculates total miles driven. ("city miles imputed"+"highway miles imputed")
    total_miles = city_miles + highway_miles
#These strings of code calculate the total MPG of both MPG conversations.
    total_city_mpg = city_miles / city_mpg
    total_highway_mpg = highway_miles / highway_mpg
#The string of code below prints the calculated MPG along with a message.
    print("You must be so proud of your mileage per gallon on your Jeep Renegade :) :")
    print("City MPG: {total_city_mpg:}")
    print("Highway MPG: {total_highway_mpg:}")
calculate_mpg()
