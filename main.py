# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students
# print(len(students))
# print(students[4]['Combo,Name'])
# print(students[4]['Email'][0])
# print(students[4]['Email'][1])
# print(students[4]['HR'])
# print(students[4]['GL'])
# for loops allow us to
#iterate through the data
#and perform some function

#we are iterating through the data
#and printing the name and email of the students
#we are also printing a line of underscores to separate the students
#we are also printing a line of underscores to separate the students
# for student in students:
#     print(student['Combo,Name'])
#     print(student['Email'][0])
#     print(student['Email'][1])
#     print(student['MName'])
#     print(student['LName'])
#     print("_"*25)


# we are asking the user to input their name
# then we are checking if the name is in the data
# if the name is in the data we are printing the name and "this works"
# name = input("what is your name? ")
# id = int(input("what is your id? "))
# for student in students:
#     if name == student['Combo,Name']:
#         print(student['Combo,Name'])
#         print("this works")


# Let's try to print out the emails of the students:    

# 4 Filter Students by Grade Level
# Print all students who are in grade 10, with details such as their full name and CPS ID
# Use a loop and a nested if statement to filter and format the output.

# grade_level = 10 # this line assigns a variable with the number '10' to be able to find all students in grade 10
# for student in students: # this is the for loop to loop through every student
#     if grade_level == student['GL']: # this line will make an if statement that will only print student's information if their grade level is 10
#         print(student['FName']) # this prints the first name
#         print(student['MName']) # this prints the middle name
#         print(student['LName']) # this prints the last name
#         print(student['CPSID']) # this prints their student id
#         print("-"*20) # this makes a line to seperate every student and their information


# 5 Format Email List for Newsletter
# Create a loop that formats and prints the email adresses of all students in a comma-seperated list.
# Use a nested for loop to ensure both primary and secondary emails are included.
        
# for student in students: # this is the for looop to loop through every student
#     print(student['Email'][0], "," , student['Email'][1]) # this prints every student's primary and secondary emails in a seperated line


# 7 Count Students by Homeroom
# Create a program that counts how many students are in each homeroom and prints the and student count.
# Use nested loops and a dictionary for counting.

# for student in students:
#    print((student['HR'][0, -1]))

# Update the dataset in memory (e.g., modify student details)
# for student in students:
#     if student['CPSID'] == 10000012:  # Example CPSID to update
#         student['FName'] = 'Jimmy'
#         student['LName'] = 'John'
#         student['GL'] = 11
#         student['HR'] = 'B218'






# for student in students:
#     if student['CPSID'] == 10000013:  # Replace with the condition to find the specific student
#         #del student['MName']  # Deletes the 'MName' key-value pair
#         #del student['GL']
#         #del student['HR']
#         #del student['Email'][0]
#         del student['LName']
#         del student['FName']
#         # Remove a specific student by index
#         del students[-1]  # Removes the first student in the list
#         print(f"Updated student: {student}")


# Update a specific entry by index
# students[2]['FName'] = 'NewName'  # Updates the first student's first name
# students[2]['LName'] = 'NewLastName'
# print(students[3])


# Example: Add a 'ContactNumber' field to each student
# for student in students:
#     if student['CPSID'] == 10000022:
#         student['ContactNumber'] = '778-988-0987'  # Assign a default or specific value


# # Create a new student dictionary
# new_student = {
#     'CPSID': 987654,
#     'Combo,Name': 'Doe, John',
#     'FName': 'John',
#     'LName': 'Doe',
#     'MName': 'Paul',
#     'HR': 'B220',
#     'GL': 11,
#     'Email': ['john.doe@example.com', 'j.doe@example.org']
# }

# # add the new student to the list
# students.append(new_student)


# # Collecting input from the user for each field
# cpsid = int(input("Enter CPSID: "))
# combo_name = input("Enter Combo,Name (Last, First): ")
# first_name = input("Enter First Name: ")
# last_name = input("Enter Last Name: ")
# middle_name = input("Enter Middle Name: ")
# homeroom = input("Enter Homeroom (e.g., B220): ")
# grade_level = int(input("Enter Grade Level: "))
# primary_email = input("Enter Primary Email: ")
# secondary_email = input("Enter Secondary Email: ")

# # Create a new student dictionary using the input
# new_student = {
#     'CPSID': cpsid,
#     'Combo,Name': combo_name,
#     'FName': first_name,
#     'LName': last_name,
#     'MName': middle_name,
#     'HR': homeroom,
#     'GL': grade_level,
#     'Email': [primary_email, secondary_email]
# }

# # Add the new student to the list
# students.append(new_student)

# # Print confirmation and the new student details
# print("New student added:")
# print(new_student)


# # Overwrite the `student_data.py` file with the updated data
# # Overwrite the student_data.py file with formatted data
# with open('student_data.py', 'w') as f:
#     f.write("students = [\n")
#     for student in students:
#         formatted_student = "    {\n"
#         for key, value in student.items():
#             formatted_student += f"        '{key}': {repr(value)},\n"
#         formatted_student = formatted_student.rstrip(",\n") + "\n    },\n"  # Clean trailing commas and newline
#         f.write(formatted_student)
#     f.write("]\n")

# print("student_data.py has been updated with the original formatting.")

# Problem 4: Insert A New Student Record

cpsid = int(input("Enter new student CPSID: "))
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
middle_name = input("Enter middle name: ")
homeroom = input("Enter homeroom: ")
grade_level = int(input("Enter grade level: "))
primary_email = input("Enter primary email: ")
secondary_email = input("Enter secondary email: ")

new_student = {
    'CPSID': cpsid,
    'Combo,Name': [last_name, first_name],
    'FName': first_name,
    'LName': last_name,
    'MName': middle_name,
    'HR': homeroom,
    'GL': grade_level,
    'Email': [primary_email, secondary_email]
}

students.append(new_student)

print(f"New student added: {new_student}")