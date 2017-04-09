'''
You are given a function f(X) = X pow 2.

You are also given K lists. The 'i'th list consists of Ni elements.

You have to pick exactly one element from each list so that the equation below is maximized:

S = (f(X1) + f(X2) +...+f(Xk))%M

Xi denotes the element picked from the 'i'th list . Find the maximized value Smax obtained.

% denotes the modulo operator.

Input Format
The first line contains 2 space separated integers K and M.
The next K lines each contains an integer Ni followed by Ni space separated integers denoting the elements in the list.

Output Format
Output a single integer denoting the value Smax.

Constraints

1 <= K <= 7
1 <= M <= 1000
1 <= Ni <= 7
1 <= Magnitude of elements in list <= 10 pow 9

Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
Sample Output

206
Explanation

Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum S value equal
to (5 pow 2 + 9 pow 2 + 10 pow 2)%1000 = 206.
'''
from itertools import product
K,M = map(int, raw_input().split())
N = product(*[[int(y)**2 for y in raw_input()[1:].split()] for _ in range(K) ])
print (max(sum(x)%M for x in N))


'''
Alternate Solution that worked only for one test case
K,M = map(int, raw_input().split())
Smax = 0
for _ in range(K):
    Smax = Smax + max(map(int, raw_input().split()[1:]))**2
print Smax
'''