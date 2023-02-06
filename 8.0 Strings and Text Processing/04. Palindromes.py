print(', '.join(sorted([x for x in set(input().split()) if x == x[::-1]], key=str.lower)))

'''
WARNING!!! 
Sometimes the sort doesn't sort exactly. (see the output from the example below)
Play in the Judge until he gives 100 points :))))

input:
Hi exe ABBA Hog fully a string ExE Bob

output: MUST BE
a, ABBA, exe, ExE
'''
