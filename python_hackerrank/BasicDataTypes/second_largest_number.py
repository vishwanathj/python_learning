'''
You are given N numbers. Store them in a list and find the second largest number.

Input Format
The first line contains N. The second line contains an array A[] of N integers each separated by a space.

Constraints
2 <= N <= 10
-100 <= A[i] <= 100

Output Format
Output the value of the second largest number.

Sample Input

5
2 3 6 6 5

Sample Output

5
'''

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    t = list(set(arr))
    t.sort(key=int, reverse=True)
    print t[1]