'''
Objective: Learn an algorithmic concept called Recursion.

Task: Write a factorial function that takes a positive integer, N as a parameter
and print the result of N!(N factorial).

Input Format: A single integet, N

Constraints
    2 <= N <=12

Output Format: Print a single integer denoting N!

Sample Input: 2
Sample Output: 6
'''

n = int(raw_input().strip())

def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

print factorial(n)