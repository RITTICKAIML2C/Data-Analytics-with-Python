# # Mini Project 
# # Employee Payroll System
# # Store:
# # Employee Name
# # Basic Salary
# # Bonus %
# # Tax %
# # Your program should calculate:
# # Annual Salary
# # Bonus Amount
# # Tax Amount
# # Final Salary
# # Display the results neatly.

employee_name = "Rittick"
basic_salary = 50000
bonus_percent = 10
tax_percent = 5

annual_salary = basic_salary * 12
bonus_amount = (annual_salary * bonus_percent) / 100
tax_amount = (annual_salary * tax_percent) / 100
final_salary = annual_salary + bonus_amount - tax_amount

print("========== Employee Payroll System ==========")
print("Employee Name :", employee_name)
print("Basic Salary  :", basic_salary, "per month")
print("Annual Salary :", annual_salary)
print("Bonus         :", bonus_percent, "%")
print("Bonus Amount  :", bonus_amount)
print("Tax           :", tax_percent, "%")
print("Tax Amount    :", tax_amount)
print("---------------------------------------------")
print("Final Salary  :", final_salary)
print("=============================================")
