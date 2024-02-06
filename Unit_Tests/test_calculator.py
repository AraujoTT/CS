from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square was not 4")
    try:
        assert square(3) == 9
    except:
        print("3 square was not 9")
    try:
        assert square(-2) == 4
    except:
        print("-2 square was not 4")
    try:
        assert square(-3) == 9
    except:
        print("-3 square was not 9")
    try:
        assert square(0) == 0
    except:
        print("0 square was not 0")

if __name__ == "__main__":
    main()
    