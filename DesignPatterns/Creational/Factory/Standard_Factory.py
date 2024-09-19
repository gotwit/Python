class A(object):
    def __init__(self):
        pass

    def show(self):
        print("Method A")

class B(object):
    def __init__(self):
        pass

    def show(self):
            print("Method B")


def get(obj=None):
    objs = dict(a=A(), b=B())
    return objs[obj]


if __name__ == "__main__":
    a = get('a')
    a.show()

    b = get('b')
    b.show()
