'''
Task: Given a base- 10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the
maximum number of consecutive 1's in n's binary representation.

Input Format

A single integer, n.

Constraints
1 <= n <= 1000000

Output Format

Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2

Explanation

Sample Case 1:
The binary representation of 5 is 101, so the maximum number of consecutive 1's is 1.

Sample Case 2:
The binary representation of 13 is 1101, so the maximum number of consecutive 1's is 2.
'''

import sys

n = int(raw_input().strip())

def decimal2binary(i):
    quotient = int(i / 2)
    remainder = int(i % 2)
    if i < 2:
        return str(remainder)
    else:
        return decimal2binary(quotient)+str(remainder)

bin = decimal2binary(n)
max = 0
curr = 0
for i in range(0, len(bin)):
    if bin[i] == str(1):
        curr+=1
    else:
        if curr > max:
            max = curr
        curr = 0
if curr > max:
    max = curr
print max
