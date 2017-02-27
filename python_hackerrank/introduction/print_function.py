'''
Read an integer N.

Without using any string methods, try to print the following:

123...N

Note that "..." represents the values in between.

Input Format
The first line contains an integer N.

Output Format
Output the answer as explained in the task.

Sample Input

3
Sample Output

123
'''

from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    for k in range(1, n+1):
        print(k, end="")
        #http://stackoverflow.com/questions/7075082/what-is-future-in-python-used-for-and-how-when-to-use-it-and-how-it-works