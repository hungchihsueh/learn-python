with open("sexy.txt", "w") as file:
    file.write("I am sexy and I know it")

data = open("sexy.txt", "r")
print(data.read())
