
results = []
 
 
def total_marks_calculate(marks):
    total = 0
    for m in marks:
        total += m
    return total
 
 
def average_marks_calculate(total, number_of_subjects):
    return total / number_of_subjects
 
 
def result_calculate(marks):
    for m in marks:
        if m < 33:
            return "Fail"
    return "Pass"
 
 
def grade_calculate(average):
    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 33:
        return "D"
    else:
        return "F"
 
 
def get_valid_marks(subject_no):
    while True:
        try:
            mark = float(input(f"Enter marks of Subject {subject_no}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100. Try again.")
        else:
            return mark
 
 
def add_result_fun():
    student_name = input("Enter Student Name: ")
    roll_number = input("Enter Roll Number: ")
 
    marks = []
    for i in range(1, 6):
        mark = get_valid_marks(i)
        marks.append(mark)
 
    total = total_marks_calculate(marks)
    average = average_marks_calculate(total, 5)
    grade = grade_calculate(average)
    result = result_calculate(marks)
 
    student = [student_name, roll_number, total, average, grade, result]
    results.append(student)
 
    print("Result added successfully!")
    print(f'''
        Student Name: {student_name}
        Roll Number: {roll_number}
        Total Marks: {total}
        Average Marks: {average:.2f}
        Grade: {grade}
        Result: {result}
    ''')
 
 
def view_results_fun():
    if len(results) == 0:
        print("No results saved yet.")
        return
 
    print("------------Student Results----------")
    for student in results:
        print(f"Name: {student[0]}, Roll: {student[1]}, Total: {student[2]}, "
              f"Average: {student[3]:.2f}, Grade: {student[4]}, Result: {student[5]}")
    print("-------------------------------------")
    print(f"Total results saved: {len(results)}")


 
while True:
    print('''
        1. Add Student Result
        2. View All Results
        3. Exit
    ''')
    choice = input("Enter your choice: ")
    if choice == '1':
        add_result_fun()
    elif choice == '2':
        view_results_fun()
    elif choice == '3':
        print("Thank you. Goodbye!")
        break
    else:
        print("Please select correct option")
 







