'''
Given 3 int values, a b c, return their sum. However, if
one of the values is 13 then it does not count towards the
sum and values to its right do not count. So for example,
if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
'''



def lucky_sum(a, b, c):
    numList = [a, b, c]
    if 13 not in numList: return sum(numList)
    else: 
        position = [a, b, c].index(13)
        newList = numList[:position]
        return sum(newList)


print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))