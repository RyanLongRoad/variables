#Ryan Cox
#16.09.2014
#stretch and challenge exercise 1 - calculate the cost to turf the garden


width = float(input("what is the total width of your garden in metres? "))

length = float(input("what is the total length of your garden in metres? "))

actualWidth = width - 2

actualLength = length - 2


area = actualWidth * actualLength
cost = area*10

print("it will cost £{0}. to turf your garden".format(cost))





