'''
@Author:Shivam Mathur
@Date:2021-06-28
@Last Modified by:Shivam Mathur
@Title: Employee Wage Computation
'''

import random


class EmployeeWageComputation:

    print("Welcome to Employee Wage Computation Program")

    def __init__(self):
        self.WAGE_PER_HOUR = 20
        self.FULL_DAY_HOUR = 8
        self.PART_TIME_HOUR = 4

    @staticmethod
    def generate_random_attendance():
        return random.randint(0, 2)

    def check_employee_attendance(self):
        '''
    Description:
        this function checks attendance .
    Parameters:
        No parameters.
    Return:
        return attendence for full and part time.
         '''
        attendance = self.generate_random_attendance()
        switcher = {
            0: 0,
            1: self.FULL_DAY_HOUR,
            2: self.PART_TIME_HOUR
        }
        return switcher.get(attendance)

    def calculate_employee_wage(self):
        '''
    Description:
        this function calculate employee wage and hours .
    Parameters:
        No parameters.
    Return:
        return total wage of employee and hours worked.
        '''
        days = 1
        employee_wage = 0
        total_wage = 0
        total_hours = 0
        while days <= 20 and total_hours <= 100:
            hours = self.check_employee_attendance()
            employee_wage = self.WAGE_PER_HOUR * hours
            print("Employee Wage for day {} is equal to {}".format(days, employee_wage))
            total_wage += employee_wage
            days += 1
            total_hours += hours
        print("Total Wage of the employee {} and he worked for total {} hours".format(total_wage, total_hours))


obj = EmployeeWageComputation()
obj.calculate_employee_wage()