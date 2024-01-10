name = input("What's your namee? ")

match name:
    case  "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")

