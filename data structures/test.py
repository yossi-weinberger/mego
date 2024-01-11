class IntNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next

    def value_to_string(self):
        return self.value


# test = IntNode(5,1)
# print (test.value)

# for i in range(4):
#    test = IntNode(i,i+1)
#    print(test.value)


# first = None
#
# for i in range(4, 0, -1):
#    temp = IntNode(i, None)
#    temp.set_next(first)
#    first = temp
#    print(f"value: {first.value} next: {first.next}")
#
# pass

first = None


for i in range(100, 0, -2):
    first = IntNode(i, first)
    print(f"value: {first.value} next: {first.next}")

temp = first
num_of = 0
sum_of = 0
max_of = 0


while temp != None:
    print(temp.value_to_string())
    num_of += 1
    sum_of += temp.value_to_string()
    if max_of < temp.value_to_string():
        max_of = temp.value_to_string()
    temp = temp.get_next()

print(num_of)
print(sum_of)
print(max_of)