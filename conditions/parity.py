def main():
    X = int(input("What's x? "))
    if is_even(X):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False


main()