# While loops and more generators and functions

# You can run a simple while loop with a conditional test that
# evaluates to True or False (or a boolean directly) and the code
# within the block will keep running while the condition is True
# and stop only when the condition evaluation turns to False

x = 0
while x < 10:
    print(x)
    x += 1

# The while loop above will print values 0 through 9 and stop when
# x reaches value of 10, at which point the condition x < 10 will
# be False since 10 < 10 is False and it will exit out of the
# while loop

# The example used in the video to find a number in a generated
# list of numbers and the index in which it was found is given below
from random import randint
l1 = [randint(1,100) for num in range(1000)]
# and we want to loop till we find the number 25, and break out once we do
i = 0
num_to_search = 25
while i < len(l1):
    if l1[i] == num_to_search:
        print(f"{num_to_search} found at index {i}")
        break
    i += 1

# The break keyword breaks out of the nearest loop it is in, if there
# are nested loops, look for the nearest for/while loop above the break
# statement

# You can use the enumerate function to get the index in an iteration
# scenario through an iterable. For example if you ran the code above
# with a for loop without tracking i, you can use enumerate like below:
l1 = [randint(1,100) for num in range(1000)]
num_to_search = 50
for index, value in enumerate(l1):
    if value == num_to_search:
        print(f"{num_to_search} found at index {index}")
        break

# While loops are most useful when you don't know when the program
# execution will end. For example, in a program where a user clicking
# on an exit button to exit the program would dictate stopping the
# loop or exiting out of the loop, example below:
while True:
    print("Please choose an option from the list below:")
    print("Press 1 for selection 1")
    print("Press 2 for selection 2")
    print("Press 3 to quit")
    selection = input("Enter your choice-> ")
    if int(selection) == 3:
        break

# We looked at another generator called zip. The zip function is
# used quite often to merge values from two lists together to form
# an iterable of the tuple values. It can cast to a list and printed
# out to show the merged list of tuples

l1 = ['.py','.js','.rb','.java','.c']
l2 = ['python','javascript','ruby','java','c']
tupled_list = list(zip(l2, l1))
print(tupled_list)

# If one list is bigger than the other, the unmatched items are
# simply ignored, for example if l2 looked like below
l2 = ['python','javascript','ruby','java','c','c++']
# and we ran the same code, c++ would be dropped and not included
# in any of the tuples
tupled_list = list(zip(l2, l1))
print(tupled_list)
