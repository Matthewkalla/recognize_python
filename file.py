num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True #variable declaration
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list declaration, initialization
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary declaration, initialization
fruit = ('blueberry', 'strawberry', 'banana') #tuple declaration, initialization
print(type(fruit)) #log statement, indicates what the type of the variable fruit is.  expected output: tuple
print(pizza_toppings[1]) #log statement. Epected output: Sausage
pizza_toppings.append('Mushrooms') #append function. adds 'Mushrooms to the pizza_toppings'
print(person['name']) #printing the value of the key 'name'  expected output: John
person['name'] = 'George' #replaces 'John' with 'George'
person['eye_color'] = 'blue' #adds the key 'eye_color' with a value of 'blue' to the person list
print(fruit[2]) #log statement.  Expected output: banana

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
"""
is an if statement.
the first statement will be evaluated as false.
therefore, the string 'It's lower' will be logged
"""
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

"""
this statement should log 'It's a long word!'
"""

for x in range(5):
    print(x) #expected output: 0, 1, 2, 3, 4
for x in range(2,5):
    print(x) #expected output: 2, 3, 4
for x in range(2,10,3):
    print(x) #expected output: 2, 5, 8,
x = 0 #variable declaration, integer initialized
while(x < 5):
    print(x)
    x += 1
"""
a while loop.  the expected output is: 0, 1, 2, 3, 4
"""

pizza_toppings.pop()
"""
if the pop method is not given a parameter, it will default
to remove the last key value and return it.
There is no variable to store the returned value, so it is thrown out.
the value popped is Olives.
"""
pizza_toppings.pop(1) #removes and returns 'Sausage"

print(person)
"""
will return: 'name': 'George', 'location': 'Salt Lake',
'age': 37, 'is_balding': False 'eye_color': 'blue'
"""
person.pop('eye_color')
"""
will remove the 'eye_color key from the person list.'
"""
print(person)
"""
will return: 'name': 'George', 'location': 'Salt Lake',
'age': 37, 'is_balding': False
"""


for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
"""
loop that steps into the pizza_toppings list.
will print 'After 1st if statement' 3 times.
"""

def print_hello_ten_times():
    for num in range(10):
        print('Hello')
"""
defines a function that will print 'Hello 10x'
"""

print_hello_ten_times()
"""
calls the function and executes the block of code
previously defined inside of that function
"""

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
"""
defines a function that will take a parameter 'x.'
it will print 'Hello' for that amount of times, starting at 0
and ending before the parameter given.
"""

print_hello_x_times(4) #log statement that will print 'Hello' 4 times.


def print_hello_x_or_ten_times(x = 10): 
    for num in range(x):
        print('Hello')
"""
defines a function that will print hello 10 times.
x is declared inside the paramenter.  if another value is given,
that will override the x value of 10.
"""

print_hello_x_or_ten_times() # the string Hello will be printed 10 times.
print_hello_x_or_ten_times(4) # the string Hello will be printed 4 times.


"""
Bonus section
"""

# print(num3) # an error will be thrown, because num3 is not yet defined.
# num3 = 72 # variable declaration, an int is initialized.


# fruit[0] = 'cranberry' # fruit is a tuple, and therefore immutable. an error will be thrown.

# print(person['favorite_team']) #there is no "favorite_team" key inside of the person list.  an error will be thrown.
# print(pizza_toppings[7]) #there is no index of 7 in the pizza_toppings list. an error will be
# print(boolean) #the variable boolean was declared as true previously.  the value 'True' will be printed
# fruit.append('raspberry') #fruit is a truple. raspberry cannot be appended.
# fruit.pop(1) #fruit is a truple.  the key at index 1 cannot be popped.