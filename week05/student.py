# student.py
# lab 5
# Author: Nur Bujang
# Write a program that stores a student name and a list of her courses and grades in a dict, 
# the program should then print out her data.
# The number of course she has could change.

# student = {
#     "name":"Mary",
#     "modules": [
#         {
#             "courseName":"Programming",
#             "grade": 45
#         },
#         {
#             "courseName":"History",
#             "grade":99
#         }
#     ]
# }
# print ("Student: {}".format(student["name"]))
# for module in student["modules"]:
#     print("\t {} \t: {}".format(module["courseName"], module["grade"]))



# Write a program that will read in the data for the data structure above, 
# ie reads in a student’s name, then keeps reading in their modules and grades
# (until the user enters a blank module name),
# You can break this up into two parts:
# a. Just read in the module names until the user enters blank,
# b. Then read in the grade as well
# This program can just read in one student (and their module details).

student = {
    "name":"Mary",
    "modules": [
        {
            "course_name":"Programming",
            "grade": 45
        },
        {
            "course_name":"History",
            "grade":99
        }
    ],
    "name":"Joe",
    "modules": [
        {
            "course_name":"Arts",
            "grade": 54
        },
        {
            "course_name":"History",
            "grade":90
        }
    ],
    "name":"Sam",
    "modules": [
        {
            "course_name":"Photography",
            "grade": 77
        },
        {
            "course_name":"Archeology",
            "grade":88
        }
    ],
    "name":"Will",
    "modules": [
        {
            "course_name":"Statistics",
            "grade": 67
        },
        {
            "course_name":"History",
            "grade":98
        }
    ]
}
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["course_name"], module["grade"]))



# If you want to go a step further, read in multiple students (until the student_name is blank).


# print (student.keys())
# for n in student["name"]:
#     print(n)
# print ("Student: {}".format(student["name"]))
# for module in student["modules"]:
#     print("\t {} \t: {}".format(module["course_name"], module["grade"]))















