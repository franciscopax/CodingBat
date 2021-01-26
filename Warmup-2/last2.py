'''
Given a string, return the count of the
number of times that a substring length 2
appears in the string and also as the last
2 chars of the string, so "hixxxhi" yields
1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''

def last2(str):
    if len(str) <= 2: return 0
    counter, appearances = 0, 0
    for _ in str:
        if str[len(str)-2:] in str[counter:counter + 2]: 
            appearances += 1
        counter += 1
    return appearances - 1


    # for _ in range(int(len(str)/2 + 2)):
    #     if str[len(str)-2:] in str[counter:counter + 2]: 
    #         appearances += 1
    #         print(f"Appearence no. {appearances}", str[counter:counter + 2])
    #     counter += 1
    # return appearances




print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
print(last2('xxaxxaxxaxx'))