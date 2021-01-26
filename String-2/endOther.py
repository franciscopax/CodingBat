'''
Given two strings, return True if either of the
strings appears at the very end of the other string,
ignoring upper/lower case differences (in other words,
the computation should not be "case sensitive").
Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
'''

def end_other(a, b):
    if len(a) == len(b): return True if a.lower() == b.lower() else False
    smallerString, largerString = min(a, b, key=len), max(a, b, key=len)
    if largerString[len(largerString) - len(smallerString):].lower() == smallerString.lower(): return True
    else: return False


print(end_other('abcXYZ', 'abcDEF'))
# print(end_other('Hiabc', 'abc'))
# print(end_other('AbC', 'HiaBc'))
# print(end_other('abc', 'abXabc'))