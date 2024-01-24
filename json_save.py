import json

person = {
    'name': 'Andrey',
    'age': 17,
    'phones': ['5445', '944999']
}

result = json.dumps(person)
print(result)
print(type(result))
