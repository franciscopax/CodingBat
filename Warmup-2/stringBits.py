'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''

def string_bits(str):
    if len(str) <= 1: return str
    newString = ""
    for n in range(0, len(str), 2):
        newString += str[n]
    return newString

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))