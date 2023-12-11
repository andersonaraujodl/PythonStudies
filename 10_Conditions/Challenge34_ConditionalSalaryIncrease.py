'''
Write a program that calculates the salary increase of an employee based on their current salary:
1. For salaries higher than $70,000.00/year, the increase will be 3.75%
2. For salaries lower, the increase will be 5%
'''

SALARY_THRESHOLD = 70000
HIGH_INCREASE = 0.0375
LOW_INCREASE = 0.05

currentSalary = float(input("What's the current salary: "))

if currentSalary > SALARY_THRESHOLD:
    salaryRaise = currentSalary * HIGH_INCREASE
else:
    salaryRaise = currentSalary * LOW_INCREASE

print("The salary raise will be {:.2f}".format(salaryRaise))