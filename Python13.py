# decorators make me want to kill myself

def test0(func):
    print("test0")
    func()
    def test1():
        print("test1")
    return test1


def test2(func):
    print("test2")
    func()
    def test3():
        print("test3")
    return test3

def func():
    print("func")


@test0
@test2

def a():
    pass

