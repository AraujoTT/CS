from hello import hello

def test_argument():
    hello('David') == 'hello, David'

def test_default():
    assert hello() == 'hello, World'