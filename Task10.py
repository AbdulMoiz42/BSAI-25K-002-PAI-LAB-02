employees = [
    ("E101", "Ali", "IT", 85000), 
    ("E102", "Sara", "HR", 75000), 
    ("E103", "Ahmed", "IT", 95000),
    ("E104", "Zain", "Finance", 90000)
]

unique_departments = {emp[2] for emp in employees}
print(f"1. Existing Departments: {list(unique_departments)}")

it_employees = [emp[1] for emp in employees if emp[2] == "IT"]
print(f"2. Employees in IT Department: {it_employees}")

salaries = [emp[3] for emp in employees]
average_salary = sum(salaries) / len(salaries)
print(f"3. Average Salary: ${average_salary:,.2f}")

highest_earner = max(employees, key=lambda emp: emp[3])
print(f"4. Highest Earner: {highest_earner[1]} (Salary: ${highest_earner[3]:,})")

dept_counts = {}
for emp in employees:
    dept = emp[2]
    if dept in dept_counts:
        dept_counts[dept] += 1
    else:
        dept_counts[dept] = 1
print(f"5. Employee Counts per Department: {dept_counts}")

employee_index = {emp[0]: (emp[1], emp[2], emp[3]) for emp in employees}

search_id = "E103"
if search_id in employee_index:
    name, dept, salary = employee_index[search_id]
    print(f"6. Fast Lookup ({search_id}) -> Name: {name}, Dept: {dept}, Salary: ${salary:,}")
else:
    print(f"6. ID {search_id} not found.")
