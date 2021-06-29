#list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#first element in the list, start with 0
print(bicycles[0])
print(bicycles[0].title())

#last element in the list
print(bicycles[-1])

#try pulling the first bicycle from the list and composing a message using that value.
message = f"My first bicycle was a {bicycles[0].title()}." 
print(message)
