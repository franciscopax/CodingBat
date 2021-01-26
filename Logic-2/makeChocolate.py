'''
We want to make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5
kilos each). Return the number of small bars to use,
assuming we always use big bars before small bars.
Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
'''

def make_chocolate(small, big, goal):
    leftover = goal - big * 5
    if leftover == 0: return 0
    else:
        if leftover < 0:
            numberOfOverusedBars = round(abs(-(leftover / 5)))
            leftover = leftover + (numberOfOverusedBars * 5)
        if leftover - (small * 1) == 0: return small
        elif leftover - (small * 1) > 0: return -1
        elif leftover - (small * 1) < 0: 
            return int(small - abs(leftover - (small * 1)))
        

print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))