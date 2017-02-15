'''
Objective: Getting started with conditional statements.

Task:
Given an integer, n, perform the following conditional actions:

    If n is odd, print Weird
    If n is even and in the inclusive range of 2 to 5, print Not Weird
    If n is even and in the inclusive range of 6 to 20, print Weird
    If n is even and greater than 20, print Not Weird

Input Format

A single line containing a positive integer, n.

Constraints
1 <= n <= 100

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Sample Input 1

24
Sample Output 1

Not Weird
'''

N = int(raw_input().strip())

if (N%2 == 1) or ( N >= 6 and N <=20):
    print 'Weird'
elif (N >= 2 and N < 5) or N > 20:
    print 'Not Weird'