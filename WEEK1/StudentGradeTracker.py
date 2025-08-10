
print("====Grade Tracker====")
print("1. Add Student")
print("2. View All Student")
print("3. Search Student")
print("4. Show Top Student")
print("5. Exit")

choose = input("Choose an Option: ")

students ={
   
}

def addStudent(name, grades):
    name = input("Student Name: ")
    students.append(name)
    for i in range(2):
        
        grade=input(f"Input Grades {i+1}: ")
        students.append(grade)

    print("Student name: ", name)
    print("Student grade: ",grade)
    return name, grade
    