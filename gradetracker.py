import statistics as s


admins = {'Cameron':'Taylor','Smith':'Faculty'}


students = {'John':[87,88,98,90],
            'Dunc':[88,67,93,90],
            'Hunter':[90,88,78,90],
            'Zach':[100,90,40,90],
            'Steve':[102,70,90,30]}

def addAssignment():
    nameToEnter = input('Assignment name:')
    TypeToEnter = input('Assignment type:')

def enterGrades():
    nameToEnter = input('Student name: ')
    gradeToEnter = input('Grade: ')
    
    if nameToEnter in students:
        print('Adding grade for'+nameToEnter)
        students[nameToEnter].append(float(gradeToEnter)) 
        print(str(nameToEnter)+' now has these grades:')
        print(students[nameToEnter])
    else:
        print('Student not found.')

def removeStudent():
    nameToRemove = input('Which student do you want to remove from the gradebook? ')
    if nameToRemove in students:
        print('Removing '+nameToRemove)
        del students[nameToRemove]
        print(students)
    else:
        print('Student not found.')

def averageStudents():
    for student in students:
        grades = students[student]
        average = s.mean(grades) 
        print(student,' average ',average)

def main():
    print("User: " + login)
    
    print("""
    Welcome to the Cam's Gradebook
    [0] - Add Asignments        
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Averages
    [4] - Log Out
    """)

    action = input('What would you like to do? (Enter a number) ')
    
    if action == '0':
                        
       addAssignment()                 
    if action == '1':
        
        enterGrades()
    elif action == '2':
        
        removeStudent()
    elif action == '3':
                
        averageStudents()
    elif action == '4':
        
        exit()
    else:
        print('Valid option not selected.') 

login = input('User: ')

if login in admins:
    password = input('Password: ')
    if admins[login] == password:
        print('Welcome,',login)
        #now run the code
        while True:
            main()
    else:
        print('Invalid password.')
else:
    print('Invalid user.')
