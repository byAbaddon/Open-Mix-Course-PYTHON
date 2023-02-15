from re import findall, match

regex = r"name\sis\s([A-z][a-z]+\s[A-z][a-z]*).+\s+([0-9]{2}) years.+on\s(\d{1,2}-\d{1,2}-\d{4})\."
name_check = r"^[A-Z][a-z]+\s[A-Z][a-z]+$"
persons = []

for line in [x for x in iter(input, 'make migrations')]:
    matches = findall(regex, line)
    if matches:
        person = list(matches)
        if not match(name_check, person[0][0]):
            continue
        persons.append([person[0][0], person[0][1], person[0][2]])

if persons:
    for i in range(len(persons)):
        print(f"Name of the person: {persons[i][0]}.")
        print(f"Age of the person: {persons[i][1]}.")
        print(f"Birthdate of the person: {persons[i][2]}.")
else:
    print("DB is empty")
    
    
'''
input:
Hello,everyone my name is Py Thon. I am 18 years old. was born on 16-10-2000.
Hello,everyone my name is Ja Va. I am 20 years old. was born on kogato si iskam.
make migrations 

output:
Name of the person: Py Thon.
Age of the person: 18.
Birthdate of the person: 16-10-2000.

'''
