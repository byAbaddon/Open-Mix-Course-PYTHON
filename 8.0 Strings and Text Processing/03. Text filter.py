lst_word, text = input().split(), input()
for w in lst_word:
   text = text.replace(w, '*' * len(w))

print(text)



'''
input:
palindrome
A palindrome is a word, *palindrome*.
output:
A ********** is a word, ************.'''