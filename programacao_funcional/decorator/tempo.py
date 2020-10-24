from functools import wraps
from time import sleep, strftime

from decorator import decorator, getfullargspec


@decorator
def logar(f, fmt="%H:%M:%S", *args, **kwargs):
    print(strftime(fmt))
    return f(*args, **kwargs)


@logar
def hello(name):
    return f"Hello, {name}"


@logar(fmt="%Y-%m-%d %H:%M:%S")
def hitchhiker():
    return 42


if __name__ == "__main__":
    print(getfullargspec(hitchhiker))
    print(getfullargspec(hello))
    print(hitchhiker())
    print(hitchhiker.__name__)
    print(hello("Gabriel"))
    print(hello.__name__)
    sleep(1)
    print(hitchhiker())
    print(hello("Renzo"))
