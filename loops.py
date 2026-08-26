#python loops
#loop through a list
#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  #Loop Through the Index Numbers
  #Use the range() and len() functions to create a suitable iterable
  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

  #using while loop.
  #You can loop through the list items by using a while loop.

#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

#Remember to increase the index by 1 after each iteration.
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

  #Looping Using List Comprehension
  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
