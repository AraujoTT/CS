with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("helli,", line, end="")


# Programing to append a name to a file
# name = input("What's your name? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")



# Programing to append a name to a list
# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f'hello, {name}')