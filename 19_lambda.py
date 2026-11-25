
square = lambda x: x*x

print(square(3))


# join method

l = [ "apple" , "orange" , "banana"]

result = "-".join(l)
print(result , l)

a = [ 1 ,2 ]
b = [1 ,2]
c = a
print(a == b) # it check for values
print(a is b) # it check that two reference point to same object
print(c == a)
print(a is c)