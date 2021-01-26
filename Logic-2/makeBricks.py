'''
We want to make a row of bricks that is goal
inches long. We have a number of small bricks
(1 inch each) and big bricks (5 inches each).
Return True if it is possible to make the goal by
choosing from the given bricks. This is a little
harder than it looks and can be done without any
loops. See also: Introduction to MakeBricks

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''


def make_bricks(small, big, goal):
    leftover = goal - (big * 5)
    if leftover == 0: return True
    else:
        if leftover < 0:
            numberOfOverusedBricks = round(abs(-(leftover / 5)))
            leftover = leftover + (numberOfOverusedBricks * 5)
        if leftover - (small * 1) <= 0: return True
        else: return False

        

print(make_bricks(3, 2, 8)) # True
print(make_bricks(1, 4, 11)) # True
# print(make_bricks(0, 3, 10)) # True

# print(make_bricks(3, 1, 8))
# print(make_bricks(3, 1, 9))
# print(make_bricks(3, 2, 10))

# print(make_bricks(3, 2, 9)) # False
# print(make_bricks(1, 4, 12)) # False
# print(make_bricks(2, 1000000, 100003)) # False