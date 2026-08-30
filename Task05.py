def add_employees(Info_Employees,IDs):
    while True:
        name=input("Enter name of employee (or enter q to quit):")
        if name.lower()=='q':
            break

        departement=input(f"Enter department for {name}:")

        salary=float(input(f"Enter salary for {name}:"))
        if salary<=0:
            print("Salary cannot be zero or negative")
            break

        job_title=input(f"Enter job title for {name}:")

        IDs+=1

        Info_Employees[IDs]={
            'name':name,
            'department':departement,
            'salary':salary,
            'job_title':job_title
        }

    return IDs

def display(Info_Employees):
    if not Info_Employees:
        print("No data")
        return

    for key,value in Info_Employees.items():
        print(f"ID: {key} | Name: {value['name']} | Department: {value['department']} | Salary: {value['salary']} | Job Title: {value['job_title']}")

def search_employee(employee_dict):
    emp_id = input("Enter Employee ID to search: ").strip()
    
    if emp_id in employee_dict:
        info = employee_dict[emp_id]
        print(f"ID: {emp_id}\nName: {info['name']}\nDepartment: {info['department']}\nTitle: {info['title']}\nSalary: ${info['salary']:.2f}")
    else:
        print("Employee ID not found.")

def update_salary(employee_dict):
    emp_id = input("Enter Employee ID to update salary: ").strip()

    if emp_id in employee_dict:
        new_salary = float(input("Enter new salary: "))
        if new_salary <= 0:
            print("Salary cannot be zero or negative!")
            return
        employee_dict[emp_id]['salary'] = new_salary
        print("Salary updated successfully.")
    else:
        print("Employee ID not found.")

def remove_employee(employee_dict):
    emp_id = input("Enter Employee ID to remove: ").strip()

    if emp_id in employee_dict:
        removed_emp = employee_dict.pop(emp_id)
        print(f"Employee {removed_emp['name']} (ID: {emp_id}) has been removed from the system.")
    else:
        print("Employee ID not found.")

if __name__=="__main__":
    Info_Employees={}
    IDs=0

    while True:
        print("\n===== HR MANAGEMENT SYSTEM =====")
        print("1. Add New Employee(s)")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Update Salary")
        print("5. Remove Employee")
        print("6. Exit program")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            IDs = add_employees(Info_Employees, IDs)
        elif choice == '2':
            display(Info_Employees)
        elif choice == '3':
            search_employee(Info_Employees)
        elif choice == '4':
            update_salary(Info_Employees)
        elif choice == '5':
            remove_employee(Info_Employees)
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Enter options 1 to 6 only")
