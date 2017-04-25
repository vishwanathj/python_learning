'''
You are given a string S.
The string contains only lowercase English alphabet characters.

Your task is to find the top three most common characters in the string S.

Input Format

A single line of input containing the string S.

Constraints

3 < len(S) < 10000

Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in ascending order.

Sample Input

aabbbccde

Sample Output

b 3
a 2
c 2

Explanation

Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c.

Note: The string S has at least 3 distinct characters.
'''
s = sorted(list(raw_input()))
l = sorted(sorted(set(s)), key=s.count, reverse=True)
for i in range(3):
    print l[i],  s.count(l[i])


'''
#Refer link(more of FYI) - http://pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/
#alternate solution that did not work for input "qwertyuiopasdfghjklzxcvbnm" that was producing output
a 1
c 1
b 1

from collections import Counter

def getKey(item):
    return item[1]

inp = Counter(list(raw_input())).most_common()
d = sorted(inp, key=getKey, reverse=True)
for i in range(3):
    print d[i][0], d[i][1]
'''

