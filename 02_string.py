st = "hello"

print(len(st))
print(st[2:4]) # 4 will be not include
print(st[-4:-1]) # negative to convert to posible like [1:4]
print(st[1:])
print(st[0:4:2])  # third one is skip


# String Functions.

print(st.endswith("o")) # give result in tru and false.
print(st.startswith("m")) # it is case sensitive
print(st.capitalize())


print(st.find("l"))  # 	Returns first index, or -1
print(st.rfind("l")) # Returns last matching index

print(st.replace("l","x") , st) # return replaced string

# name = input("Enter your name ");
# print(name)

