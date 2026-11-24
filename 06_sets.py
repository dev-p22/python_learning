d = { } # Empty Dict

es = set() # empty set
# set don't hold duplicate values.

s= { 2 ,33 ,5 ,2 ,3 ,5 ,5 ,5 ,5 , "lala"}
print(s)# it return distict values elements.


# methods.
s.add(4)
print(s) # It is unorder  , unindexed , no way to change items in set
# print(s[2]) # it give error.

s.remove(4)
print(s)


s1 = { 22 ,11 , 44 }
s2 = { 33 , 44 , 11}

print(s1.union(s2))
print(s1.intersection(s2))