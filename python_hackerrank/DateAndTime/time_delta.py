'''
Timestamps are given in the format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. See the sample below for details.

Task
Given 2 timestamps, print the absolute difference (in seconds) between them.

Input Format
The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t1 and time t2.

Output Format
Print the absolute difference (t1 - t2) in seconds.

Constraints
It is guaranteed that the input contains only valid timestamps, and the year can reach up to 3000.

Sample Input

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 +0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 +0000
Sample Output

25200
88200
'''

#Refer:https://docs.python.org/2.7/library/datetime.html#strftime-strptime-behavior

from datetime import datetime

format = '%a %d %b %Y %X %z'
#seems like %z is supported only in python 3 and not in python 2
for _ in range(int(input())):
    t1=datetime.strptime(input(), format)
    t2=datetime.strptime(input(), format)
    print (int(abs((t1-t2).total_seconds())))