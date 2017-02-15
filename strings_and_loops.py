'''
Objective: Combine knowledge of strings and loops

Task:
Given a string, S, of length N that is indexed from O to N - 1, print its even-indexed and odd-indexed
characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input Format

The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a String, S.

Constraints

1 <= T <= 10
2 <= length of S <= 10000

Output Format

For each String Sj (where 0 <= j <= T -1), print Sj's even-indexed characters, followed by a space,
followed by Sj's odd-indexed characters.

Sample Input

2
Hacker
Rank

Sample Output

Hce akr
Rn ak

'''

numTests = int(raw_input().strip())

for j in range(0, numTests):
    s = str(raw_input().strip())
    even = ''
    odd = ''
    length = len(s)
    for k in range(0, int(0.5*length)+1):
        try:
            even += s[2*k]
            odd += s[2 * k + 1]
        except IndexError:
            break
    print even+" "+odd
