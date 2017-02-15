#!/bin/python

import sys

'''
Objective
Demonstrates learning about the Array data structure.

Task
Given an array, A, of  N integers, print A's elements in reverse order as a single line of space-separated numbers.

Input Format

The first line contains an integer, N (the size of our array).
The second line contains N space-separated integers describing array A's elements.

Constraints

1 <= n <= 1000

1 <= Ai <= 10000, where Ai is the 'i'th integer in the array.
Output Format

Print the elements of array A in reverse order as a single line of space-separated numbers.

Sample Input

4
1 4 3 2
Sample Output

2 3 4 1
'''

# https://docs.python.org/2/library/functions.html#raw_input
n = int(raw_input().strip())
# https://docs.python.org/2/library/functions.html#map
arr = map(int,raw_input().strip().split(' '))

# https://docs.python.org/2/library/functions.html#reversed
print " ".join(str(item) for item in reversed(arr))
