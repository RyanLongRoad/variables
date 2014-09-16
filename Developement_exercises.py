#Ryan Cox
#12/09/2014
#Development exercises - calculates the remainder that results after division

import math

number1 = int(input("Please enter number 1: "))

number2 = int(input("Please enter number 2: "))

answer = int(number1//number2)

remainder = int(number1%number2)

print("The answer is {0} and the remainder is {1}.".format(answer, remainder))
