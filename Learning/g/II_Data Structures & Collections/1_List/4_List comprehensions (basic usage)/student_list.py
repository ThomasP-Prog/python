def sorted_list(student_list : list[dict]) -> list[dict]:
    sort = [student for student in student_list
                if isinstance(student.get("grade"),(int|float)) and student.get("grade")>90]
    return sorted(sort, key = lambda x:x["name"])



def main() -> None:
    students = [
    {"name": "Leo", "grade": 89},
    {"name": "Sophia", "grade": 91},
    {"name": "Jack", "grade": 95},
    {"name": "Eve", "grade": 74},
    {"name": "Paul", "grade": 77},
    {"name": "Hannah", "grade": 81},
    {"name": "Ryan", "grade": 79},
    {"name": "Alice", "grade": 85},
    {"name": "Charlie", "grade": 92},
    {"name": "David", "grade": 67},
    {"name": "Olivia", "grade": 93},
    {"name": "Ian", "grade": 76},
    {"name": "Mia", "grade": 72},
    {"name": "Quinn", "grade": 86},
    {"name": "Karen", "grade": 83},
    {"name": "Bob", "grade": 78},
    {"name": "Tom", "grade": 82},
    {"name": "Noah", "grade": 80},
    {"name": "Frank", "grade": 88},
    {"name": "Grace", "grade": 90},
]
    grade_90 = sorted_list(students)
    if grade_90:
        print("Students with above 90")
        for student in grade_90:
            print(f"{student.get('name')} with a grade of {student.get('grade')}")

if __name__ == "__main__":
    main()