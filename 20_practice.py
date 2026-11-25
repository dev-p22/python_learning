st = "amazing values"

s = st[::-1]
print(s)
print("".join(reversed(st)))


l = [ 12 , 24, 4, 5, 36, 63, "lala"]

# l.reverse() # it rever list but modify orignal

print(l[::-1]) # it will no modify orignal ones.
print(l)


str = "programming"
result = ""

for char in str:
    if char not in result:
        result += char


print(result)

