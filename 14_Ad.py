# advand type Hints
from typing import list

# walrus operator

if(n := len([1,2,3,4,5])) > 3:
    print(f"List is {n} elements long")


# Type definations
n : int= 5

def sum(a:int,b:int)->int:
    return a + b;

sum(2,3)

number : list[int] = [3,42,424,235]




