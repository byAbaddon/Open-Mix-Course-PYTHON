text, f_type = input(), input()
if f_type == 'LOWERCASE':
    print('The total sum is:', sum([ord(x) for x in text if x.isalpha() and x == x.lower()]))
else:
    print('The total sum is:', sum([ord(x) for x in text if x.isalpha() and x == x.upper()]))

'''
input:
HelloFromMyAwesomePROGRAM
LOWERCASE
output:
The total sum is: 1539
'''
