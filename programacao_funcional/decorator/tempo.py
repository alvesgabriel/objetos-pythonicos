from functools import wraps
from time import sleep, strftime


def logar(f):
    @wraps(f)
    def run_with_time(*args, **kwargs):
        print(strftime("%H:%M:%S"))
        return f(*args, **kwargs)

    return run_with_time


@logar
def hello(name):
    return f"Hello, {name}"


@logar
def hitchhiker():
    return 42


if __name__ == "__main__":
    print(hitchhiker())
    print(hitchhiker.__name__)
    print(hello("Gabriel"))
    print(hello.__name__)
    sleep(1)
    print(hitchhiker())
    print(hello("Renzo"))
