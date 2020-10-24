from functools import wraps
from time import sleep, strftime


def logar(fn=None, *, fmt="%H:%M:%S"):
    if fn is not None:
        return logar(fmt=fmt)(fn)

    def decorator(f):
        @wraps(f)
        def run_with_time(*args, **kwargs):
            print(strftime(fmt))
            return f(*args, **kwargs)

        return run_with_time

    return decorator


@logar
def hello(name):
    return f"Hello, {name}"


@logar(fmt="%Y-%m-%d %H:%M:%S")
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
