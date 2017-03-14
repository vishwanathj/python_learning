'''
You are given a string S. Your task is to capitalize each word of S.

Input Format

A single line of input containing the string, S.

Constraints
0 < len(S) < 1000
The string consists of alphanumeric characters and spaces.

Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, S.

Sample Input

hello world
Sample Output

Hello World
'''

def capitalize(string):
    new_str_list = list(string)
    for i in range(len(new_str_list)):
        if i == 0:
            new_str_list[i] = new_str_list[i].upper()
        elif new_str_list[i-1] == ' ':
            new_str_list[i] = new_str_list[i].upper()
    return ''.join(new_str_list)

if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string