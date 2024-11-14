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

for student in students:
    print((student['HR'][0, -1]))