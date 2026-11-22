def units_calculate(previous_reading, current_reading):
    return current_reading - previous_reading

def energy_charge_calculate(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return (100 * 5) + (units - 100) * 7
    else:
        return (100 * 5) + (100 * 7) + (units - 200) * 10

def vat_calculate(energy_charge):
    return energy_charge * 0.05

def total_bill_calculate(energy_charge, vat):
    return energy_charge + vat

def add_bill_fun():
    customer_name = input("Enter Customer Name: ")
    meter_number = input("Enter Meter Number: ")

    while True:
        previous_reading = float(input("Enter Previous Reading: "))
        if previous_reading <= 0:
            print("Please enter positive value.")
        else:
            break

    while True:
        current_reading = float(input("Enter Current Reading: "))
        if current_reading <= 0:
            print("Please enter positive value.")
        elif current_reading <= previous_reading:
            print("Current Reading must be greater than Previous Reading.")
        else:
            break

    units = units_calculate(previous_reading, current_reading)
    energy_charge = energy_charge_calculate(units)
    vat = vat_calculate(energy_charge)
    total_bill = total_bill_calculate(energy_charge, vat)

    print("-----Bill Info---------")
    print(f'''
        Customer Name: {customer_name}
        Meter Number: {meter_number}
        Units Consumed: {units}
        Energy Charge: {energy_charge}
        VAT: {vat}
        Total Bill: {total_bill}
    ''')

    with open('bills.txt', 'a') as file:
        file.write(f'Customer Name: {customer_name}, Meter Number: {meter_number}, Units: {units}, Total Bill: {total_bill}\n')
    print("Bill saved successfully.")

def view_bill_fun():
    with open('bills.txt', 'r') as file:
        content = file.read()
        print(f'''
        ------------Bill History----------
        {content}
        ''')

# create bills.txt if it does not exist (old bills are kept)
with open('bills.txt', 'a') as file:
    pass

while True:
    print('''
        1. Add Customer Bill
        2. View All Bills
        3. Exit
    ''')
    choice = input("Enter your choice: ")
    if choice == '1':
        add_bill_fun()
    elif choice == '2':
        view_bill_fun()
    elif choice == '3':
        break
    else:
        print('Please select correct option')