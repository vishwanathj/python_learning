'''
Task
Read a line of input from stdin and save it to a variable, s. Then print the contents of s to stdout.

Input Format

A single line containing sentence s.

Constraints

1 <= \s| <= 500

Output Format

Print the contents of s to stdout.

Sample Input

How many chickens does it take to cross the road?

Sample Output

How many chickens does it take to cross the road?
'''

def read():
    s = raw_input()
    return s

if __name__ == '__main__':
    my_str = read()
    print my_str