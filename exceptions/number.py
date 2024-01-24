def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(pronpt):
    while True:
        try:
            return int(input(pronpt))
        except ValueError:
            pass

main()