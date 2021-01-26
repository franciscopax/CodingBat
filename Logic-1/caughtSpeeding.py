'''
You are driving a little too fast, and a police officer
stops you. Write code to compute the result, encoded as
an int value: 0=no ticket, 1=small ticket, 2=big ticket.
If speed is 60 or less, the result is 0. If speed is between
61 and 80 inclusive, the result is 1. If speed is 81 or more,
the result is 2. Unless it is your birthday -- on that day,
your speed can be 5 higher in all cases.

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
'''

def caught_speeding(speed, is_birthday):
    lowerLimit = 60 if not is_birthday else 65
    midLimit = 80 if not is_birthday else 85

    if speed <= lowerLimit:
        return 0
    elif speed > lowerLimit and speed <= midLimit:
        return 1
    elif speed > midLimit + 1:
        return 2

print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))