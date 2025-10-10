# LESSON #8. Словари (dict) и работа с ними
from multiprocessing.connection import address_type

countries = {
    'code': 'UA',
    'name': 'Ukraine',
    'population': 50
}

for key, value in countries.items():
    print(f"{key}: {value}")

print(f"\ncountries.get('code'): {countries.get('code')}")

print(f"\ncountries.keys(): {countries.keys()}")

print(f"\ncountries.values(): {countries.values()}")

countries.popitem()
print(f"\ncountries.popitem(): {countries}")

countries.pop('code')
print(f"\ncountries.pop('code'): {countries}")

countries.clear()
print(f"\ncountries.clear(): {countries}")

person = {
    'user': {
        'first_name': 'Jhon',
        'last_name': 'Marley',
        'age': 45,
        'address': {
            'city': 'New-York',
            'street': 'Broadway',
            'house': 52
        }
    }
}

print(f"\nperson['user']['address']['city']: {person['user']['address']['city']}")
