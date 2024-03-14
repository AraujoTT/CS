class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

    # using a dictionary to return
    # return {"name":input("Name: "), "house":input("house: ")}

    # Using the list to return the value
    # name = input("Name: ")
    # house = input("house: ")
    # return [name, house]

if __name__ == "__main__":
    main()