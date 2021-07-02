## MODIFY
#Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
#modify the 1st element
motorcycles[0] = 'ducati' 
print(motorcycles)

## APPEND
#Adding Elements to the end of a list
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
#append element to the end of the list
motorcycles.append('ducati') 
print(motorcycles)


##another example for append function to an empty list
motorcycles = []
motorcycles.append('honda') 
motorcycles.append('yamaha') 
motorcycles.append('suzuki')
print(motorcycles)

##extend function is to append a list/multiple items to an existing list
motorcycles = ['honda', 'yamaha', 'suzuki'] 
test = ['toyota', 'audi']
motorcycles.extend(test)
print(motorcycles)


## INSERT
#Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
#insert an element in the 1st position
motorcycles.insert(0, 'ducati') 
print(motorcycles)
#then insert an element in the 5th position
motorcycles.insert(4, 'toyota') 
print(motorcycles)


## REMOVE
#Removing Elements from a List
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
#delete the 1st element
del motorcycles[0] 
print(motorcycles)
#then delete the 2nd element
del motorcycles[0] 
print(motorcycles)


#Removing an Item Using pop() or remove()
##The pop() method removes the last item in a list, but it lets you work with that item after removing it.
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
#removing last element from motorcycles and save the last element to popped_motorcycle
popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)

#another example for pop
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

#Popping Items from any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#Removing an Item by Value - using remove() function
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
motorcycles.remove('ducati') 
print(motorcycles)

#another example for remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


#The remove() method deletes only the first occurrence of the value you specify
motorcycles = ['honda', 'yamaha', 'ducati', 'ducati'] 
print(motorcycles)
motorcycles.remove('ducati') 
print(motorcycles)
