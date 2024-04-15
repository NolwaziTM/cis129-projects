# Module 11: Lab 11
# Author:Nolwazi Moyo
# Date : 04/14/2024

import csv

# Exercise 9.1: Writing grades to a plain text file
def write_grades_to_file():
    with open("grades.txt", "w") as file:
        print("Enter grades (enter -1 to finish): ")
        while True:
            grade = int(input("Enter grade (-1 to finish): "))
            if grade == -1:
                break
            file.write(str(grade) + "\n")

# Exercise 9.2: Reading grades from a plain text file
def read_grades_from_file():
    with open("grades.txt", "r") as file:
        grades = [int(grade.strip()) for grade in file.readlines()]
    total = sum(grades)
    count = len(grades)
    average = total / count if count > 0 else 0
    print("Individual grades:", grades)
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)

# Exercise 9.3: Writing student records to a CSV file
def write_student_records_to_csv():
    with open("grades.csv", "w", newline="") as csvfile:
        fieldnames = ["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        while True:
            first_name = input("Enter student's first name (or press Enter to finish): ")
            if not first_name:
                break
            last_name = input("Enter student's last name: ")
            exam1_grade = int(input("Enter exam 1 grade: "))
            exam2_grade = int(input("Enter exam 2 grade: "))
            exam3_grade = int(input("Enter exam 3 grade: "))
            writer.writerow({"firstname": first_name, "lastname": last_name, "exam1grade": exam1_grade, "exam2grade": exam2_grade, "exam3grade": exam3_grade})

# Call the functions
write_grades_to_file()
read_grades_from_file()
write_student_records_to_csv()
