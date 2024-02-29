import csv

name = input("What's your name? ")
home = input("where's your home? ")

with open("students.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


# code using for read a csv file with csv,DictReader introducing how to read a cv file with name of columns and save in a dict
# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home":row["home"]})

#     # for line in file:
#     #     name, home = line.rstrip().split(",")
#     #     student = {"name": name, "home": home}
#     #     students.append(student)

# # def get_name(student):
# #     return student["name"]

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")



# Open a file and read after show the name of the student
# and the house
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")