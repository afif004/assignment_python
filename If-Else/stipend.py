lvl = int(input("Level: "))
smstr = int(input("Semester: "))
cgpa = float(input("CGPA: "))

c = cgpa * 50
base_stipend = (lvl - 1) * 200 + 500 + (smstr - 1) * 100

stpnd = base_stipend + c
print(f"Stipend = {stpnd:.2f}")
