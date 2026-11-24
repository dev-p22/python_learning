# f = open("file.txt")
# data = f.read()
# print(data)
# f.close() 

# above can be write as 
with open("file.txt") as f:
    print(f.read())

# st = "jfdalfadls;fjadls;d adsladsfaldsfjas. dfklkaddflj"
# f = open("writeTest.txt","w")
# f.write(st);
# f.close()