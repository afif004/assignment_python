def calculate_stipend(level, semester, cgpa):
    c = cgpa * 50
    base_stipend = (level - 1) * 200 + 500 + (semester - 1) * 100
    return base_stipend + c

level = int(input("Level: "))
semester = int(input("Semester: "))
cgpa = float(input("CGPA: "))
stipend = calculate_stipend(level, semester, cgpa)
print(f"Stipend = {stipend:.2f}")