name, age, town, salary = [input() if not x & 1 else float(input()) for x in range(4)]

age_range = {age < 18: 'teen', 18 <= age < 70: 'adult', age >= 70: 'elder'}
salary_range = {salary < 500: 'low', 500 <= salary < 2000: 'medium', salary >= 2000: 'high'}

print(f'Name: {name}\nAge: {int(age)}\nTown: {town}\nSalary: ${salary:.2f}')
print(f'Age range: {age_range[True]}\nSalary range: {salary_range[True]}')

'''
input:
Gosho
20
Sofia
530

output:
Name: Gosho
Age: 20
Town: Sofia
Salary: $530.00
Age range: adult
Salary range: medium
'''
