# Variable Declaration
num1 = 42  # Data Type integer
num2 = 2.3  # Data Type float
boolean = True  # Data Typem --> Boolean
string = 'Hello World'  # Data Type --> String

# Data type --> List
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# Data type --> Dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# Data type --> Tuples
fruit = ('blueberry', 'strawberry', 'banana')

# Printing the data in python.
print(type(fruit))
print(pizza_toppings[1])

# List method to add the data at the end.
pizza_toppings.append('Mushrooms')

# printing the data from name key in person dictionary.
print(person['name'])

# Change of value assigned to the key name in person dictionary.
person['name'] = 'George'

# Change of value assigned to the key eye_color in person dictionary.
person['eye_color'] = 'blue'

# Print the third item in fruit list.
print(fruit[2])

# Use of If statement in python
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# Use of If elseif statement in python.
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# For loop in the python with number of execution.
for x in range(5):
    print(x)

# For loop in python with start and stop. Start --> Inclusive, Stop --> Exclusive.
for x in range(2, 5):
    print(x)

# For loop in python with start, stop and increment value.
for x in range(2, 10, 3):
    print(x)

# While loop in python.
x = 0
while x < 5:
    print(x)
    x += 1

# Removing last item from the pizza_topping list.
pizza_toppings.pop()

# Removing item at index 1 from the pizza_topping list.
pizza_toppings.pop(1)

# Removing the key : value pair from person dictionary.
print(person)
person.pop('eye_color')
print(person)

# Iterating through each topping in pizza topings.
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break


# Python function declration
def print_hello_ten_times():
    for num in range(10):
        print('Hello')


# Execution of the already declared function.

print_hello_ten_times()


# Passing argument in the python function declration.

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')


# Execution of the already declared function.

print_hello_x_times(4)


# Setting of the default value in the function declration.

def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')


# Execution of the already declared function with and without passing argument.

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

"""
Bonus section
"""

# print(num3) --> Name Error
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean) --> Indentation Error
# fruit.append('raspberry')
# fruit.pop(1)
