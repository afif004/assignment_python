def print_student_info(roll):
    students = [
        (1, "Ali", 20),
        (2, "Babar", 22),
        (3, "Chad", 21)
    ]
    
    for student in students:
        if student[0] == roll:
            print(f"Name: {student[1]}")
            print(f"Age: {student[2]}")
            return

roll = int(input())
print_student_info(roll)