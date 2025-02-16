my_numbers = [1, 4, 3, 7, 2, 6]

def multiply(numbers_list, multiplier):
    multiplied_list = []

    for number in numbers_list:
        multiplied_list.append(number * multiplier)
    
    return multiplied_list

print(multiply(my_numbers, 3)) 
print(my_numbers)                 
