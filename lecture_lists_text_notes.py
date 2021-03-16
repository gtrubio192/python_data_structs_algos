## Lists, both lectures 1 and 2
# Lists are mutable
# I have 3 lists declared below, play around with the following
# functions, methods, slices or other ones you like on them
# len(), min(), max(), append(), insert(), extend(), remove(), pop()
# reverse(), sort(), count()
# Note: Some methods/functions above are covered in lecture 1
# while others are covered in lecture 2

my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10, 15]
my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
my_new_list = ["art", "econ"]
print(f"Ints: {my_list}")
print(f"Strings: {my_strings_list}")
print(f"New list: {my_new_list}")

# Write your function or method code here
# sorted() is a function that sorts not in place, returns new list
my_sorted_list = sorted(my_list)
# sort() object method sorts list IN PLACE
my_list.sort()

# 'in' returns true/false if your list contains something
print("physics" in my_strings_list)
# index() obj method returns position of searched object w/in list
print(my_strings_list.index("physics"))
# dir() function prints a list of available methods you can use for a list(or whatever data type you have)
print(dir(my_list))
# count() func returns the number of times an item occurs in a list
my_list.count(15)

# append() adds to end of list
my_list.append(25)
#insert() , first arg is the position where you want to insert something, 2nd arg is the value
my_list(4, 666)
# extend() is like JS concat, it adds a new array to end of existing array
my_strings_list.extend(["something", "new"])
# slicing - some_list[start:end-1].
# this will slice/return [15, 6, 7, 8, 35]
print(my_list[0:5])
# reverse a list. '::' is saying go from start-end, but begin with last element (-1)
print(my_list[::-1])

# reverse() does same thing
my_list.reverse()

print("My altered lists...")
print(my_list)
print(my_strings_list)
print(my_new_list)
