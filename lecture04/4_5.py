import time


def my_decorator(func):
    def wrapper(arg):
        print("obertka")
        start = time.perf_counter()
        func(arg)
        print('time of working ', time.perf_counter() - start)
        print("finish")
    return wrapper


@my_decorator
def myfunc(x):
    print("sleep", x)
    time.sleep(x)


myfunc(3)
