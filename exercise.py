# SIMPLEST - Restaurant Waiter Helper

# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

# DOD
# its own project on your laptop and Github
# be git tracked
# have 5 commits mininum!
# has documentation
# follows best practices

# starter code
menu = ['falafel', 'HuMMus', 'coUScous', 'Bacalhau a Bras']


print ('Menu Items:')
print(menu[0].title())
print(menu[1].title())
print(menu[2].title())
print(menu[3].title())


food_order = []

food_order.append(input('What would you like to order first?'))
print(food_order)

food_order.append(input('What would you like to order second?'))
print(food_order)

food_order.append(input('What would you like to order third?'))
print(food_order)



# I need to print each item from the list
# print(menu[0])
# before I print I need to make them all capitalized
#  print everything