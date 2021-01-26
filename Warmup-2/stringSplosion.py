'''
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''

def string_splosion(str):
    newString = ""
    counter = 0
    for _ in str:
        counter += 1
        newString += str[0:counter]
    return newString

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))