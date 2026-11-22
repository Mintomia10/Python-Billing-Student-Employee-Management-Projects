records = []

def house_rent_calculate(basic_salary):
    return basic_salary * 0.40

def medical_allowance_calculate(basic_salary):
    return basic_salary * 0.10

def gross_salary_calculate(basic_salary, house_rent, medical_allowance):
    return basic_salary + house_rent + medical_allowance

def tax_calculate(gross_salary):
    if gross_salary >= 50000:
        return gross_salary * 0.10
    elif gross_salary >= 30000:
        return gross_salary * 0.05
    else:
        return 0

def net_salary_calculate(gross_salary, tax):
    return gross_salary - tax

def add_salary_fun():
    employee_name = input("Enter Employee Name: ")
    employee_id = input("Enter Employee ID: ")
    designation = input("Enter Designation: ")

    while True:
        basic_salary = float(input("Enter Basic Salary: "))
        if basic_salary <= 0:
            print("Please enter positive value.")
        else:
            break

    house_rent = house_rent_calculate(basic_salary)
    medical_allowance = medical_allowance_calculate(basic_salary)
    gross_salary = gross_salary_calculate(basic_salary, house_rent, medical_allowance)
    tax = tax_calculate(gross_salary)
    net_salary = net_salary_calculate(gross_salary, tax)

    record = [employee_name, employee_id, gross_salary, tax, net_salary]
    records.append(record)

    print("-----Salary Info---------")
    print(f'''
        Employee Name: {employee_name}
        Employee ID: {employee_id}
        Designation: {designation}
        Basic Salary: {basic_salary}
        House Rent: {house_rent}
        Medical Allowance: {medical_allowance}
        Gross Salary: {gross_salary}
        Tax: {tax}
        Net Salary: {net_salary}
    ''')
    print("Salary record added successfully.")

def view_records_fun():
    if len(records) == 0:
        print("No salary records saved yet.")
    else:
        print("------------Salary Records----------")
        for record in records:
            print(f"Name: {record[0]}, ID: {record[1]}, Gross Salary: {record[2]}, Tax: {record[3]}, Net Salary: {record[4]}")
        print(f"Total salary records saved: {len(records)}")

while True:
    print('''
        1. Add Employee Salary
        2. View All Records
        3. Exit
    ''')
    choice = input("Enter your choice: ")
    if choice == '1':
        add_salary_fun()
    elif choice == '2':
        view_records_fun()
    elif choice == '3':
        break
    else:
        print('Please select correct option')