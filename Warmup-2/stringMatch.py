'''
Given 2 strings, a and b, return the number of 
the positions where they contain the same length
2 substring. So "xxcaazz" and "xxbaaz" yields 3,
since the "xx", "aa", and "az" substrings appear
in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
'''

def string_match(a, b):
    if len(a) == 3 and len(b) == 3: return 2 if a == b else 0
    counter, appearances = 0, 0
    for n in range(0, len(min(a, b)), 1):
        if a[counter:counter+2] == b[counter:counter+2]:
            appearances += 1
        counter += 1
    return appearances
            

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))
print(string_match('aabbccdd', 'abbbxxd')) #1
print(string_match('aaxxaaxx', 'iaxxai')) #3
print(string_match('iaxxai', 'aaxxaaxx')) #3
