#Ryan Cox
#18.09.2014
#a program to display an amount of money as the minimum amount
 
money = int(input("Please enter the amount of mone you have: "))
twenties = money//20
remainder1 = money%20
tens= remainder1//10
remainder1 = remainder1%10
fives = remainder1//5
remainder1 = remainder1%5
twos = remainder1//2
remaider1 = remainder1%2
ones = remainder1//1



print("the number of twenty pound notes you need is: {0}".format(twenties))

print("the number of ten pound notes you need is: {0}".format(tens))

print("the number of five pound notes you need is: {0}".format(fives))

print("the number of two pound notes you need is: {0}".format(twos))

print("the number of one pound notes you need is: {0}".format(ones))
      
