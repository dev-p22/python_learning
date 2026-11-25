# it is like array container to store any values.
# it is mutable unlike string
friends = [ 3 ,5 , "Apple" , "orange" , False , "Lala"];

print(friends)
print(friends[3])

# friends[1] = 50;
# print(friends);

# same indexing as string
print(friends[3:5])

#in string it was returning new string but in list it will change orignal list.
#list methods
friends.append("Company")

# friends.reverse()
# friends.sort() # it gave eror if string values present in list

friends.insert(2,34343434) # insert 34343434 such that it index will be 2
friends.remove("Company")
print(friends)


#q1 
fruits = []

f1 = input("Enter Fruit Name :")
fruits.append(f1)
print(fruits)

l2 = [ 12,34,352,52]
print(sum(l2))

l3 = [0 ,32 , 0 , 3452 , 0 ,23 , 0 ,3 ,0 ,5 , 3 , 2 ,0 , 0 , 0]
print(l3.count(0))


# append and extend
l2 = [ 1 ,2 ,3 ]

l2.append([4,5]) # adds one object as a single element.

print(l2)

l2.extend([6,7])

print(l2) # adds each element from an iterable to the existing list.