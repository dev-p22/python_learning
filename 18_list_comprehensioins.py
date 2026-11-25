# it is way to make list bases on existing list

myList = [ 1 ,24 ,35, 3, 2, 3 ,9 ,1]

# Aam jindagi
# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

# mantos life
squaredList = [i * i for i in myList]
print(squaredList)    


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = [num for num in numbers if num % 2 ==0]
print(even)