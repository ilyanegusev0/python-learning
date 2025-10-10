# LESSON #6. Функции строк. Индексы и срезы

text = "soccer, Basketball, tennis, Volleyball, baseball, Rugby, american football"

print(f"\ntext: {text}")

if not text.isupper():
    print(f"\nupper(): {text.upper()}")

if not text.islower():
    print(f"\nlower(): {text.lower()}")

print(f"\ncapitalize(): {text.capitalize()}")

print(f"\nfind('tennis'): {text.find('tennis')}")

sports = text.split(', ')

for el in range(len(sports)):
    sports[el] = sports[el].capitalize()

print(f"\ntext.split(', '): {sports}")

text = ", ".join(sports)
print(f"\n\", \".join(sports): {text}")

# Срезы

word = 'FFoooottbbaallll'
print(f"\nword[0:8:2] + word[8::2]: {word[0:8:2]} + {word[8::2]}")  # first:end:step
