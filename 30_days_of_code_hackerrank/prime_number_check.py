'''
Task
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Given a number, n, determine and print whether it's Prime or Not prime.


Input Format

The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines contains an integer, n, to be tested for primality.

Constraints
1 <= T <= 30
1 <= n <= 2000000000


Output Format

For each test case, print whether n is Prime or Not prime on a new line.

Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime
Explanation

Test Case 0: .
12 is divisible by numbers other than 1 and itself (i.e.: 2, 3, 6), so we print Not prime on a new line.

Test Case 1: n = 5.
5 is only divisible 1 and itself, so we print Prime on a new line.

Test Case 2: n = 7.
7 is only divisible 1 and itself, so we print Prime on a new line.
'''

T = int(raw_input())
a = []
for i in range(T):
    a.append(int(raw_input()))

for j in range(T):
    flag = True
    if a[j] > 1:
        for k in range(2, a[j]/2):
            if (a[j] % k) == 0:
                flag = False
                break
        if flag:
            print 'Prime'
        else:
            print 'Not prime'
    else:
        print 'Not prime'