#access items
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #it will print the second item

#negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#range of negative indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") #Check if "apple" is present in the list
