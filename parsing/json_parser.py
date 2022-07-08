import json

with open('parsing/students.json', 'r') as students:
  students_list = json.load(students)


  input_str = 'm'

  for student in students_list:

    if student['Class'] == input_str:
        print(student)

    elif student['Club'] == input_str:
        print(student)

    elif student['Gender'] == input_str.upper():
        print(student)
        

