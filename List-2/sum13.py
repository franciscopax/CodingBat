'''
Return the sum of the numbers in the array, returning 0 for an
empty array. Except the number 13 is very unlucky, so it does
not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
'''

def sum13(nums):
    if len(nums) == 0: return 0
    sum = 0
    for i in range(0, len(nums)):
        sum += nums[i]
        if nums[i] == 13:
            sum -= nums[i]
        elif i > 0 and nums[i - 1] == 13:
            sum -= nums[i]
    return sum





# print(sum13([1, 2, 2, 1, 13]))
print(sum13([1, 2, 2, 1]))
