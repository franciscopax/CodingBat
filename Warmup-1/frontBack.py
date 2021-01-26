'''
Given a string, return a new string where
the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''

def front_back(string):
    if len(string) <= 1: return string
    else: return string[len(string) - 1] + string[1:len(string) - 1] + string[0]

# Test
print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
