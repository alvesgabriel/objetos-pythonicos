a = 5


def f(a=3):
    b = 3
    print(globals())
    print(locals())
    print(f"a = {a}")
    print(f"b = {b}")


class A:
    a = 41
    a += 1
    print(a)
    print(globals())
    print(locals())


# f()
