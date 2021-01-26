'''
Return the number of times that the string "code" appears anywhere
in the given string, except we'll accept any letter for the 'd',
so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
'''

def count_code(str):
  appearances = 0
  for i in range(0, len(str) - 1, 1):
    if str[i:i + 2] == "co" and str[i + 3] == "e": appearances += 1
    if i + 3 == len(str) - 1: break 
  return appearances

print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))
