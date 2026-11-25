# collection of key-value pair
# lookup is fast in it.
marks = {
    "a" : 10,
    "b" : 34,
    "c" : 44,
    "list" : [2,35,3],
    0:'hello',
    0:343 # First 0 value will be over riden by second 0 value.
}

print(marks["a"]) # it give error if don't exits.
print(marks['list'])

# unorderd , mutable , indexed , can't contain duplicate key

#methods
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"a": 9,"z":33}) # if key-value present then it will update if not then it will insert new one.
print(marks)

print(marks.get("a")) # it give none if doesn't exit on dict


