# For loops for iterating through iterables and list comprehension

# List comprehension - powerful way to generate lists by embedding a for loop inside a list declaration
from random import randint, choice
from string import ascii_uppercase
# this list comprehension does a loop 100 times, and appends a random int(from 1-100) each time
l1 = [randint(0,100) for num in range(100)]
# this loop does exact same as above statement!
l2 = []
for num in range(100):
    l2.append(randint(0,100))

# With list comprehension, you can also generate any type of values.
# this prints 100 randomdly chosen upper case letters
l3 = [choice(ascii_uppercase) for num in range(100)]
print(l3)
# For the list defined below, we explored two ways of iterating
# through the list and calculating the sum of all elements in it
l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

sum = 0
for num in l:
    sum += num
print(f"Sum using list: {sum}")

# Same calculation done using range generator, which gives us an iterable
sum = 0
for num in range(len(l)):
    sum += l[num]
print(f"Sum using range generator: {sum}")

# Range is a very useful generator if you don't know ahead of time how many times
# you want an iteration in a for loop to take place, example below
# with an input received from the user
run_times = int(input("How many times do you want the program to run? "))
for num in range(run_times):
    print(f"Run: {num+1}")

# You can also use range generator to create a list quickly
print(list(range(10)))

# You can also give it a start and end val, as well as step size
# this generates a list of 1-20, printing every odd number
list(range(1,20, 2))

# You can generate a list of random integers using the range function
# in combination with the randint function from the random module
from random import randint
l1 = []
for num in range(25):
    l1.append(randint(1, 100))
print(l1)
print(len(l1)) # Checking the number of integers generated

# You can do the same using list comprehension in 1 line below
l1 = [randint(1,100) for num in range(25)]
print(l1)
print(len(l1)) # Checking the number of integers generated

# You can use the items method to get an iterable from a dictionary
# then you can iterate through the tuples of key value pairs that
# this provides to print them out, or use them in other ways

my_dict = {'py': 'python', 'rb': 'ruby', 'js': 'javascript'}
for k, v in my_dict.items():
    print(f"Extension of .{k} means it's a {v} program")
