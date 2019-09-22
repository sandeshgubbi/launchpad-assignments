numbers = [input("enter 5 random numbers: ") for i in range(5)]
def remove(numbers): 
    new_list = [] 
    for num in numbers: 
        if num not in new_list: 
            new_list.append(num)
    return new_list           
print(remove(numbers)) 