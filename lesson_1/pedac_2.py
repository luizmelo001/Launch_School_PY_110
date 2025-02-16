"""
Given a list of strings, sort the list based on the highest number of adjacent consonants a string contains and 
return the sorted list. 
If two strings contain the same highest number of adjacent consonants,they should 
retain their original order in relation to each other. 
Consonants are considered adjacent if they are next to each other in the same word or 
if there is a space between two consonants in adjacent words.
"""

def count_adjacent_consonants(str):
    VOWELS = set('aeiouAEIOU')
    counter = 0
    str_list = list(str)
    first_letter = str_list.pop(0)

    for letter in str_list:
        if first_letter and letter not in VOWELS:
            counter += 1
            
        first_letter = letter
    return counter


def sort_by_consonant_count(lst):
    consonant_dict = {}

    for word in lst:
        consonant_dict.update({word: 0})
        consonant_dict[word] = count_adjacent_consonants(word.strip())

    sorted_consonant_count = sorted(consonant_dict, key=consonant_dict.get, reverse=True)

    print(consonant_dict)
    return sorted_consonant_count

print(count_adjacent_consonants('dddaa'))

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list) ==  ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan']
#print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])

my_list = ['bar', 'car', 'far', 'jar']
#print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])


my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])

my_list = ['xxxa', 'xxxx', 'xxxb']
#print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa'])
