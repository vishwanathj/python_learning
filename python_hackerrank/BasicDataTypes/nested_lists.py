'''
Given the names and grades for each student in a Physics class of N students, store them in a nested list and
print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name
on a new line.

Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name,
and the second line contains their grade.

Constraints

* 2 <= N <= 5
There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students,
order their names alphabetically and print each one on a new line.

Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output

Berry
Harry

Explanation

There are 5 students in this class whose names and grades are assembled to build the following list:

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we
order their names alphabetically and print each name on a new line.
'''

# reference link : http://stackoverflow.com/questions/8002374/is-there-any-way-to-sort-nested-lists-without-using-operator-itemgetter

import operator
l = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    t = [name, score]
    l.append(t)

l.sort(key=operator.itemgetter(1))
minima = l[0][1]
second_min = None
second_list = []

for item in l:
    if not second_min:
        if item[1] > minima:
            second_min = item[1]
            second_list.append(item)
    elif item[1] == second_min:
        second_list.append(item)
    elif item[1] > second_min:
        break
second_list.sort(key=operator.itemgetter(0))

for item in second_list:
    print item[0]
