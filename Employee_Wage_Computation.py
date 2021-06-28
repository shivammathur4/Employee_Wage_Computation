'''
@Author:Shivam Mathur
@Date:2021-06-28
@Last Modified by:Shivam Mathur
@Title: Employee Wage Computation
'''

import random

print("Welcome to Employee Wage Computation Program")
attendance = random.randint(0, 2)
if attendance == 0:
    print("Absent")
elif attendance == 1:
    print("Present")