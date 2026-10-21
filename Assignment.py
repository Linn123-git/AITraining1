name = input("Enter student name: ")
age = int(input("Enter student age: "))
mark = float(input("Enter student mark: "))

print("Name:", name)
print("Age:", age)
print("Mark:", mark)

if mark >= 80:
    print("Grade A")
elif mark >= 60:
    print("Grade B")
elif mark >= 40:
    print("Grade C")
else:
    print("Fail")

for i in range(1, 4):
    print("Subject", i)

def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

marks = [80, 75, 90]
average = calculate_average(marks)

print("Average mark:", average)

marks = [80, 75, 90] 

subjects = ("English", "Math", "Science")

student = {
    "name": "Mg Mg",
    "age": 18,
    "average": 81.67
}

print(marks)
print(subjects)
print(student)