def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    return {"name":input("Name: "), "house":input("house: ")}

    # name = input("Name: ")
    # house = input("house: ")
    # return [name, house]

if __name__ == "__main__":
    main()