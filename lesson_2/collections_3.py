"""
Given the object shown below, print the name, age, and gender of each family member:
"""

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for key, value in munsters.items():
    print(f"{key} is a {munsters[key]['age']}-year-old {munsters[key]['gender']}.")