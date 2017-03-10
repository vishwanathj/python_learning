'''
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each
command will be of the 7 types listed above. Iterate through each command in order and perform
the corresponding operation on your list.

Input Format

The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

if __name__ == '__main__':
    N = int(raw_input())
    list = []
    for i in range(N):
        alist = map(None, raw_input().strip().split(' '))
        operation = alist[0]
        if operation == 'insert':
            list.insert(int(alist[1]), int(alist[2]))
        elif operation == 'print':
            print list
        elif operation == 'remove':
            list.remove(int(alist[1]))
        elif operation == 'append':
            list.append(int(alist[1]))
        elif operation == 'sort':
            list.sort(key=int)
        elif operation == 'pop':
            list.pop()
        elif operation == 'reverse':
            list.reverse()