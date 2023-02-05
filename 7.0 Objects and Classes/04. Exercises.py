lst = [x.split(' -> ') for x in iter(input, 'go go go')]

for token in lst:
    print(f'Exercises: {token[0]}')
    print(f'Problems for exercises and homework for the "{token[1]}" course @ SoftUni.')
    print(f'Check your solutions here: {token[2]}')
    token = token[3:][0].split(', ')
    for i in range(0, len(token)):
        print(f'{i + 1}. {token[i]}')

'''
input:
ObjectsAndSimpleClasses -> ProgrammingFundamentalsExtended -> https://judge.softuni.bg/Contests/439 -> Exercises, OptimizedBankingSystem, Animals, Websites, Boxes, BoxIntersection, Messages
go go go
output:
Exercises: ObjectsAndSimpleClasses
Problems for exercises and homework for the "ProgrammingFundamentalsExtended" course @ SoftUni.
Check your solutions here: https://judge.softuni.bg/Contests/439
1. Exercises
2. OptimizedBankingSystem
3. Animals
4. Websites
5. Boxes
6. BoxIntersection
7. Messages
'''
