"""ou have a list of tuples, where each tuple contains a student's name, subject, and score:
   grades = [('Alice', 'Math', 88), ('Bob', 'Math', 92), ('Alice', 'History', 95),
   ('Charlie', 'Math', 75), ('Bob', 'History', 85)].
   Create a nested dictionary where the outer keys are the student names,
   and the inner value is another dictionary mapping subjects to scores for that student."""

import collections

def tuple_to_dict(grades : list[tuple[str,str,int]]) -> dict[str,dict[str,int]]:
    """take a list and return a dict"""
    if not grades:
        return {}
    
    student_dict = collections.defaultdict(dict) # Creates inner dict if needed
    for name, subject, grade in grades:
        student_dict[name][subject] = grade
    return student_dict

def print_dict(grades : dict[str,dict[str,int]]) -> None:
    """print formatted dict"""
    if not grades:
        return
    else:
        max_name_len = 0
        max_subject_len = 0
        
        # Get max length
        for name,subjects in grades.items():
            max_name_len = max(max_name_len,len(name))
            for subject in subjects.keys():
                max_subject_len = max(max_subject_len,len(subject))

        # Add padding
        max_name_len += 1
        max_subject_len += 1

        # Header
        print(f"{'Name':<{max_name_len}} {'Subject':<{max_subject_len}} Grade")
        print("-" * (max_name_len + max_subject_len + len('grade')+2))

        # Sort by name and subject
        for name in sorted(grades.keys()):
            subjects = grades[name]
            for subject in sorted(subjects.keys()):
                grade = subjects[subject]
                print(f"{name:<{max_name_len}} {subject:<{max_subject_len}} {grade}")


def main() -> None:
    """main function"""
    grades = [('Alice', 'Math', 88), ('Bob', 'Math', 92), ('Alice', 'History', 95), ('Charlie', 'Math', 75), ('Bob', 'History', 85)]

    student_dict = tuple_to_dict(grades)
    print(student_dict)
    print_dict(student_dict)

if __name__ == "__main__":
    main()