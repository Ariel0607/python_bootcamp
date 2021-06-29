## SORT
#Sorting a List Permanently with sort() - the sort is permanently in alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

##sort this list in reverse alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) 
print(cars)

#Sorting a List Temporarily with sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:") 
print(sorted(cars))
print("\nHere is the original list again:") 
print(cars)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# a = sorted(cars)
# print(cars)
# print(a)


##Printing a List in Reverse Order - using reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() 
print(cars)


##Finding the Length of a List - using len()
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
len(cars)
#range of a list is always [0, len-1], so it's [0,3] in the above example
##IndexError: list index out of range when running below
print(cars[4])

