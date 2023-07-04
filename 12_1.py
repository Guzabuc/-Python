import json

# pets = {
#     'name': 'Barsic',
#     'age': 12,
#     'meals': ['Purina', 'Hills', 'Hm'],
#     'owner': {'fname': 'Sam', 'sname': 'Black'}
# }
#
# with open ('pets.json', 'w') as pet_file:
#     json.dump(pets, pet_file)
with open('pets.json') as pet_file:
    string = pet_file.read()
    data = json.loads(string)

for item in data:
    if type (data[item]) == list:
        print(item, ', '.join(data[item]))
    elif type(data[item]) == dict:
        for k , v in data[item].items():
            print(k, v)
    else:
        print(data[item])