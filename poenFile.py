list = []
with open("poem.txt") as f:
    for line in f:
        print(line, end="")
        list.append(line)
        print(list)
