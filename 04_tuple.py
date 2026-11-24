# tuple is immutable unlike list 

a = ( 1, 2 ,5 ,33 ,66 ,99 , False , "lala" , 5 )
b = (2,) # if you write (2) then it consider is as int , for tuple add , at last for single value
print(type(a))
print(a)

# tuple methods.
print(a.count(5))
print(a.index(5)) # return first index of occured element
print(33 in a)

#unpacking
t1 = (1 ,2 ,3)
c , d,e = t1
print(c,d,e)


