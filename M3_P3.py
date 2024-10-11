#Corinthian M
#Oct 8, 2024 
#This program calculates the area for a circle.
#Line 10 Code to prompt the user to enter the radius for their desired circle.      
# "I didnt relize I had to "import "math". Math was required to use visual studios version of pi. So i had to ask google how to get pi working on visual studio."
#line 10-11 - Code to calculate the area for a circle.
#line 12-14 - Code to print the result of the conversion.
import math
def main():
    radius = float(input("Please enter the radius of the circle:"))
    area = math.pi * radius * 2
    print("The area of the circle with radius {radius} is: {area:}")
if __name__ == "__main__":
    main()
