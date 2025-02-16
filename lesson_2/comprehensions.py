"""
Compute and display the total age of the family's male members. 
Try working out the answer two ways: first with an ordinary loop, then with a comprehension.
"""

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

total_age = 0

for name, info in munsters.items():
    print(info)
    if info['gender'] == 'male':
        total_age += munsters[name]['age']

print(total_age)

all_male_age = [member['age'] for member in munsters.values() if member['gender'] == 'male']
print(sum(all_male_age))


"""
Given the following data structure, return a new list with the same structure, 
but with the values in each sublist ordered in ascending order. 
Use a comprehension if you can. (Try using a for loop first.)
"""

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

lst = [sorted(sublist) for sublist in lst]
print(lst)


"""
Given the following data structure, write some code that defines a dictionary where the key is the first item in each sublist, 
and the value is the second.
"""

lst_1 = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

dict_1 = dict(lst_1)
print(dict_1)


"""
Given the following data structure, sort the list so that the sub-lists 
are ordered based on the sum of the odd numbers that they contain. You shouldn't mutate the original list.
"""

def sum_of_odd_numbers(lst):
    odd_numbers = [n for n in lst if n % 2 != 0]
    return sum(odd_numbers)

lst_2 = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

sorted_list = sorted(lst_2, key=sum_of_odd_numbers)
print(sorted_list)


"""
Given the following data structure, return a new list identical in structure to the original but, with each number incremented by 1.
Do not modify the original data structure. Use a comprehension.
"""

def increment_values(dictionary):
    return {key: value + 1 for key, value in dictionary.items()}

lst_3 = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
lst_3 = [increment_values(value) for value in lst_3]

print(lst_3)

"""
Given the following data structure return a new list identical in structure to the original, 
but containing only the numbers that are multiples of 3.
"""


def multiples_of_three(lst):
    return [num for num in lst if num % 3 == 0]


lst_4 = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
new_list = [multiples_of_three(lst) for lst in lst_4]

#for list in lst_4:
#    temp_lst = []
#    for val in list:
#        if val % 3 == 0:
#            temp_lst.append(val)
#    new_list.append(temp_lst)

print(new_list)    
    

"""
Given the following data structure, write some code to return a list that contains the colors of the fruits and the sizes of the vegetables. 
The sizes should be uppercase, and the colors should be capitalized.
"""

dict2 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def transform_item(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    else:
        return item['size'].upper()

result = [transform_item(item) for item in dict2.values()]
print(result)
        
"""
Given the following data structure, write some code to return a list that contains only the dictionaries where all the numbers are even.
"""

lst_5 = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
    
def has_only_even(dictionary):
    for sublist in dictionary.values():
        for value in sublist:
            if value % 2 != 0:
                return False
    return True
            
even_dict_list = [d for d in lst_5 if has_only_even(d)]

print(even_dict_list)

"""
Write a function that takes no arguments and returns a string that contains a UUID.


Problem
    Input: 
        -no arguments

    Output: 
        -UUID STRING

    Rules
        -5 sections in an 8-4-4-4-12 pattern
        -32 hexadecimal characters (the digits 0-9 and the letters a-f)

    Questions

Examples
    'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'

Data Type
    -List
    -String

Algorithim
    -Create an empty list to hold each section of the UUID
    -Loop through to create 5 sections of the UUID
        *For the first section, generate 8 chars
        *For the next three sections, generate 4 characters each
        *For the last section generate 12 characters
    -Helper function for random chars:
        *takes a lenght parameter
        *Uses a strin gof hexadecimal characters (0-9, a-f)
        *Rnadomly selects and join characters to match the given lenght
    -Construct the UUID
        *Use a conditional logic to determine the lenght of each section based on its positions
    -Combine the sections with hypens

Code
...

"""

import string, random

def random_digits_and_letters(lenght):
    hex_chars = '0123456789abcdef'
    return ''.join(random.choice(hex_chars) for i in range(lenght))

def uuid_generator():
    result = []

    for i in range(1,6):
        match i:
            case 1:
                result.append(random_digits_and_letters(8))
            case 5:
                result.append(random_digits_and_letters(12))
            case _:
                result.append(random_digits_and_letters(4))

    return "-".join(result)


print(uuid_generator())

"""
The following dictionary has list values that contains strings. 
Write some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, then print it.


Problem
    Input:
        -Dictionaty

    Output:
        -List of string of each word in the values of the dictionary

    Rules

    Questions

Examples
    - ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

Data Type
    -Dictionaty
    -List

Algorithim
    -Extract the values of the dictionary
    -Loop through each list
    -Loop through each word in the list
    -Split the word into individual chars 
    -append the chars into an empty list set to a variable called result
    -Return the value of result

Code
...

"""

dict_3 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

#result = []

#for lst in dict_3.values():
#    for word in lst:
#        for char in list(word):
#            if char in 'aeiou':
#                result.append(char)            



result_11 = [char for lst in dict_3.values()
               for word in lst
               for char in list(word) if char in 'aeiou']

print(result_11)