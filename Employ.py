
# To add records
def add_employees(employee_dict, emp_id, name , department):
    if emp_id not in employee_dict:
        employee_dict[emp_id]={"Name":name, "Department": department}
        print('Employee added successfully')
    else:
        print("Employee id already present!")

def remove_employee(employee_dict, emp_id):
    if emp_id in employee_dict:
        del employee_dict[emp_id]
        print("Employee removed successfully!")
    else:
        print("Employee Id not found")

def update_employee(employee_dict, emp_id, name , department):
    if emp_id in employee_dict:
        if name:
            employee_dict[emp_id]['Name']=name
        if department:
            employee_dict[emp_id]['Department']= department

        print("Employee updated successfully!")
    else:
        print("Employee id not found...")

# To display records
def list_employee(employee_dict):
    print("\n\n Employee records....")
    if not employee_dict:
        print("No employees to display")
    for emp_id, details in employee_dict.items():
        print(f"ID: {emp_id}, Name: {details['Name']}, Department: {details['Department']}")



# python main function
if __name__=="__main__":
    # a dictionary to store employee record
    employees = {}
    while True:
        print(
            "\n========Employee Management System========"
        )
        print("Press 1: To add employee...")
        print("Press 2: To remove employee...")
        print("Press 3: To update employee...")
        print("Press 4: To list employee...")
        print("Press 5: To Exit...")

        choice = int(input("\n Enter your choice (1,2,3,4,5)...."))
        print(f"You entered: '{choice}'")  # Debugging line

        if choice == 1:
            id = int(input("Enter employee id:"))
            name = input("Enter employee name:")
            department = input("Enter employee department:")
            add_employees(employees, id, name, department)

        elif choice== 2:
            id=int(input("Enter Employee id...."))
            remove_employee(employees, id)

        elif choice == 3:
            id = int(input("Enter Employee id...."))
            name = input("Enter Employee name (if blank)....")
            department = input("Enter Employee department (if blank)....")
            update_employee(employees, id, name if name else None, department if department else None) # list comprehension

        elif choice == 4:
            list_employee(employees)

        elif choice == 5:
            print("Exiting the system....")
            break

        else:
            print("Please enter correct choice!")