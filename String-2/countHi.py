'''
Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
'''

def count_hi(str):
    appearances = 0
    for i in range(0, len(str) - 1, 1):
        if str[i:i+2] == 'hi': appearances += 1
        if i + 2 == len(str): break
    return appearances

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))