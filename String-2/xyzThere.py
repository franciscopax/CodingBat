'''
Return True if the given string contains an appearance of
"xyz" where the xyz is not directly preceeded by a
period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
'''

def xyz_there(str):
    if len(str) < 3: return False
    appearance = 0
    for i in range(0, len(str) - 1, 1):
        if str[i:i+3] == 'xyz':
            if i == 0: appearance += 1
            else: 
                if str[i - 1] != '.': appearance += 1
    return True if appearance > 0 else False




print(xyz_there('abc.xyzxyz'))

print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))