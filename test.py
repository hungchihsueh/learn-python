# print(map(str, [[96], [69]]))
# print(list(map(str, [[96], [69]])))
# print(''.join(list(map(str, [[96], [69]]))))

numbers = [15, 30, 47, 82, 95]


def lesser(numbers):
    return numbers < 50


small = list(filter(lesser, numbers))
print(small)


class MyFirstClass:
    print("who wrote this?")
    index = "Author-Book"
    def handle_list(self,philosopher,book):
        
        