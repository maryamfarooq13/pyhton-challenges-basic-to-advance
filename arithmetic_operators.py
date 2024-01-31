# You have 100 rupees to buy a ticket of movie.
# Each ticket costs 12 rupees. Write a python program to calculate how many tickets you can buy.
print('Price of a ticket is Rs.12')
print('Rupees you have: 100')
price_of_a_ticket = 12
total_rupees = 100
tickets = price_of_a_ticket//total_rupees
print(f'You can buy {tickets} in Rs. 100') # OR print('you can buy, tickets, in Rs. 100)

print('\n')

# In the last three cricket games, babar azam scored 22, 28, and 35.
# write a python score to Calculate his average score per game.
print('Score of Babar Azam in three Cricket games is as follows:')
print('In first game: 22')
print('In second game: 28')
print('In Third game: 35')
game1 = 22
game2 = 28
game3 = 35
average = (game1+game2+game3)/3 #DMAS rule is not followed in python
print(f'Average score of Babar Azam in three cricket games is {average}')

print('\n')

# You're building a rectangular garden that's 20 feet long and 15 feet wide.
# Calculate the total length of fencing needed to enclose the garden.
# do not use if else. only use operators and print fundction
print('To find the length of fencing around a garden of:')
print('20 feet long')
print('15 feet wide')
length_of_gardern = 20
width_of_garden = 15
fencing = 2*(length_of_gardern*width_of_garden) #logical error because farmula is L+W
print(f'Total length of fencing to enclose the garden is {fencing} feet')

print('\n')

# If each pizza can serve 3 people, 
# write a program to find out how many pizzas are needed for a party of 27 people.
print('How many pizza are needed for a party of 27 people?')
print('A pizza can serve 3 peaople')
people_to_serve = 27
serving_per_pizza = 3
reqired_pizzas = people_to_serve//serving_per_pizza
print(f'{reqired_pizzas} pizzas are required to serve 27 people')

print('\n')

# If your bike uses 3 liters of fuel per 100 km and fuel costs 262 rupees per liter,
# how much will the fuel cost for a 400 km trip? write a python code for that.

print('what will be the cost for 400 km trip if:')
print('one liter costs Rs.262 and')
print('three liter fuel is used per 100 km')
cost_of_fuel_perliter = 262
distance_of_trip = 400
# 3 liter for 100km
# ? liter for for 400km (3*4)
print('How much liter of fuel for 1 km?')
distance = 100
fuel = 3
liter_per_km = 3/100
print(f'{liter_per_km} liter of fuel is required per km')
print('How much liter of fuel for 400 km?')
liter_for_trip = 400*liter_per_km
print(f'{liter_for_trip} liter of fuel is required for 400 km trip')
cost_of_fuel_trip = 12*cost_of_fuel_perliter
print(F'Cost of fuel will be {cost_of_fuel_trip} Rupees for a 400 km trip')

print('\n')

# Write a program that asks the user for the diameter of a sphere and then computes the
# 1. Volume
# 2. Surface Area
# Use the value of 𝜋 i.e. 3.142, as a constant.
# Volume of a sphere = 4/3 𝜋𝑟^3
# Surface Area = 4𝜋r^2

# Radius:
diameter = int(input('Enter Diameter of Sphere: '))
radius = diameter/2
print ('Radius of Sphere:', radius)
#1 Volume
v1 = 4/3
v2 = v1*3.142     #you can also create a variable pi=3.142 OR in a single step
v3 = radius**3      # Another way: v = ((4/3)*3.14*radius**3)
volume = v2*v3
print('Volume of Sphere:', volume)
#2 Surface Area
sa1 = 4*3.142
sa2 = sa1*radius**2
SurfaceArea = sa2
print ('Surface Area of Sphere:', SurfaceArea)