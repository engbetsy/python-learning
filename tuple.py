thistuple = ("apple", "banana", "cherry")
print(thistuple)
#tuple length
#To determine how many items a tuple has, use the len() function
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Create Tuple With One Item
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Create an Empty Tuple
#To create an empty tuple, use round brackets with no content.
thistuple = ()
print(type(thistuple))

#Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

#type()From Python's perspective, tuples are defined as objects with the data type 'tuple'
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
