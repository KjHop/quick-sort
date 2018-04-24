from SortingClass import Sorting

operator = Sorting()
entering = True

print ("Enter numbers u want to sort (press enter when you want to enter another number, spaces will not be taken into consideration)")
#Allow user to enter his own list of numbers
while entering:
    number = input("Enter number $ ")
    if number == "stop":
        entering = False
        break
    number=number.replace(" ", "")
    #Check if user entered number
    try:
        number = int(number)
        operator.addNumber(number)
    except ValueError:
        entering = True
#Print return of quicksort
print(operator.quickSort(operator.returnList()))