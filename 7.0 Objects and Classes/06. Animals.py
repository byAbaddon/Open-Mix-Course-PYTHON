lst_data = [x.split() for x in iter(input, 'I\'m your Huckleberry')]
lst_sound = [x for x in lst_data if len(x) == 2]

# make sound
for token in lst_sound:
    a_type = [x[0] for x in lst_data if x[1] == token[1]][0]
    if a_type == "Dog":
        print('I\'m a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.')
    if a_type == 'Cat':
        print('I\'m an Aristocat, and I will now produce an aristocratic sound! Myau Myau.')
    if a_type == 'Snake':
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")

sort_lst = sorted(lst_data, key=lambda x: (x[0] == 'Dog', x[0] == 'Cat', x[0] == 'Snake'), reverse=True)
for x in [x for x in sort_lst if len(x) > 2]:
    if x[0] == 'Dog':
        other = 'Number Of Legs:'
    elif x[0] == 'Cat':
        other = 'IQ:'
    else:
        other = 'Cruelty:'
    print(f'{x[0]}: {x[1]}, Age: {x[2]}, {other} {x[3]}')

# --------------------------------------------(2) ----------------------------------------
'''
class Dog:
    def __init__(self, name, age, number_of_legs):
        self.name = name
        self.age = age
        self.number_of_legs = number_of_legs
        self.sound = 'I\'m a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.'

    def produce_sound(self, ):
        print(self.sound)


class Cat:
    def __init__(self, name, age, intelligence_quotient):
        self.name = name
        self.age = age
        self.intelligence_quotient = intelligence_quotient
        self.sound = 'I\'m an Aristocat, and I will now produce an aristocratic sound! Myau Myau.'

    def produce_sound(self, ):
        print(self.sound)


class Snake:
    def __init__(self, name, age, cruelty_coefficient):
        self.name = name
        self.age = age
        self.cruelty_coefficient = cruelty_coefficient
        self.sound = "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."

    def produce_sound(self, ):
        print(self.sound)


lst_data = [x.split() for x in iter(input, 'I\'m your Huckleberry')]
lst_animals = []
dog = Dog
cat = Cat
snake = Snake

for token in lst_data:
    if len(token) == 2:  # animal make sound
        _, a_name = token
        animal_for_class = [x.__class__.__name__ for x in lst_animals if x.name == a_name]
        if animal_for_class:
            if animal_for_class[0] == "Dog":
                dog.produce_sound()
            if animal_for_class[0] == 'Cat':
                cat.produce_sound()
            if animal_for_class[0] == 'Snake':
                snake.produce_sound()
            continue
    else:
        a_type, a_name, a_age, a_other = token
        if a_type == 'Dog':
            dog = Dog(a_name, a_age, number_of_legs=a_other)
            lst_animals.append(dog)
        if a_type == "Cat":
            cat = Cat(a_name, a_age, intelligence_quotient=a_other)
            lst_animals.append(cat)
        if a_type == 'Snake':
            snake = Snake(a_name, a_age, cruelty_coefficient=a_other)
            lst_animals.append(snake)

sort_lst = sorted(lst_data, key=lambda x: (x[0] == 'Dog', x[0] == 'Cat', x[0] == 'Snake'), reverse=True)
# print(lst_data)
# print(sort_lst)

for x in [x for x in sort_lst if len(x) > 2]:
    if x[0] == 'Dog':  other = 'Number Of Legs:'
    elif x[0] == 'Cat':other = 'IQ:'
    else: other = 'Cruelty:'
    print(f'{x[0]}: {x[1]}, Age: {x[2]}, {other} {x[3]}')
'''

'''
input:
Dog Sharo 3 4
Cat Garfield 5 200
Snake Alex 25 1000
talk Sharo
talk Garfield
talk Alex
I'm your Huckleberry

output:
I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.
I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.
I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.
Dog: Sharo, Age: 3, Number Of Legs: 4
Cat: Garfield, Age: 5, IQ: 200
Snake: Alex, Age: 25, Cruelty: 1000
'''
