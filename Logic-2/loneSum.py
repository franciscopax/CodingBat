'''
Given 3 int values, a b c, return their sum. However, if one of
the values is the same as another of the values, it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
'''

def helper(a, b, c):
    return 0 if a in [b, c] else a

def lone_sum(a, b, c):
    return helper(a, b, c) + helper(b, a, c) + helper(c, b, a)

print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))