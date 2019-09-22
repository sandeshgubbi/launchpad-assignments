numbers = [int(input("enter any random value: ")) for i in range(4)]
def add(numbers):
    new_list=[]
    for i in numbers:
        if i < 5:
            new_list.append(i)
    return new_list
print(add(numbers))