# it helps to show error instead of crashing. (show Enter valid number)

try:
    a = int(input("Enter Number : "))
    print(a)
except ValueError as v:
    print(v , "valueerror")
except Exception as e:
    print(e)    
else: # if try block successful execute then else will call other wise it will not called.
    print("I am inside else")
finally: # it will run for both try and except / it use in function even if we return before it it run evern if function return.
    print("I am inside finally")

# b = input("Enter Number : ") # this is wrogn code just for raise example

# print(type(b))
# if(type(b) != int ):
#     raise TypeError("You can't enter other data types")
