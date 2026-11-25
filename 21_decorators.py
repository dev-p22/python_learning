# A decorator in Python is a function that adds extra functionality 
# to another function without changing its original code.
import time


# aam life
# def greet():
#     print("Hello!")

# def decorator(func):
#     def wrapper():
#         print("Before function execution")
#         func()
#         print("After function execution")

#     return wrapper

# greet = decorator(greet)

# greet()


def decorator(func):
    def wrapper():
        print("Before func run")
        func()
        print("After func run")
    return wrapper;    


def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time : ", end - start)
    return wrapper

@decorator
@calculate_time
def greet():
    print("Hello!")

greet()

@calculate_time
def xyz():
    print("xyz")


xyz()