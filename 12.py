import json

pets = {
    'name': 'Barsic',
    'age': 12,
    'meals': ['Purina', 'Hills', 'Hm'],
    'owner': {'fname': 'Sam', 'sname': 'Black'}
}

with open ('pets.json', 'w') as pet_file:
    json.dump(pets, pet_file)

# 'a' - добывить