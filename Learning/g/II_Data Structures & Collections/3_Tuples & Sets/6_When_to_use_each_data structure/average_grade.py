"""Write a function calculate_average_grades that takes a dictionary 
   where keys are student names (strings) and values are lists of integer grades they received. 
   The function should return a new dictionary where keys are the student names and values are their average grade (float).
"""
from typing import Mapping

def calculate_average_grades(students : Mapping[str,list[int]]) -> dict[str,float]:
    """ Return average grade of the students"""
    average_grades = {}
    for student,grades in students.items():
        if len(grades) > 0:
            average_grades[student] = round(sum(grades) / len(grades),2)
        else:
            average_grades[student] = 0
    return average_grades

def print_average_grades(student_average : dict[str,float]) -> None:
    """format average grades"""
    if not student_average:
        print("No student found")
        return
    print("Students average grades :")
    print("-"*25)
    for student,average in student_average.items():
        print(f"{student} : {average}")

def main() -> None:
    """main function"""
    student_grades_input = {
        'Alice': [85, 90, 92, 88],
        'Bob': [78, 80, 84],
        'Charlie': [95, 98],
        'Diana': []
    }
    student_average = calculate_average_grades(student_grades_input)
    print_average_grades(student_average)

if __name__ == "__main__":
    main()