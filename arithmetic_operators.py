'''
Objective: Work with arithmetic operators.

Task: Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Input Format:
There are 3 lines of numeric input:
The first line has a double, mealCost (the cost of the meal before tax and tip).
The second line has an integer, tipPercent  (the percentage of mealCost being added as tip).
The third line has an integer, taxPercent (the percentage of mealCost being added as tax).

Output Format:
Print The total meal cost is totalCost dollars., where totalCost is the rounded integer result of the entire bill
(mealCost with added tax and tip).

Sample Input

12.00
20
8

Sample Output

The total meal cost is 15 dollars.

'''

mealCost = float(raw_input().strip())
tipPercent = int(raw_input().strip())
taxPercent = int(raw_input().strip())

tip = mealCost*tipPercent*0.01
tax = mealCost*taxPercent*0.01
totalCost = int(round(mealCost+tip+tax))

print "The total meal cost is "+str(totalCost)+" dollars."