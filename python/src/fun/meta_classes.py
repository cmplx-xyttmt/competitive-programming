import functools
import sys
import copy


class AnnouncerMeta(type):
    """
    Print method name when called.

    FIXME Something is wrong here, please fix it.

    Solution: Use __init__ instead of __new__
    Another solution: pass func

    The issue is a closure bug.
    """

    def __new__(cls, class_name, bases, namespace):
        namespace_copy = copy.deepcopy(namespace)
        for name, func in list(namespace.items()):
            if callable(func):

                @functools.wraps(func)
                def call_wrapper(*args, f=func, **kwargs):
                    try:
                        return f(*args, **kwargs)
                    finally:
                        print(f"Called {f.__name__}")

                # if name in ['foo', 'bar']:
                #     print(name, "->", call_wrapper)
                namespace_copy[name] = call_wrapper

        # print(namespace_copy)

        return type.__new__(cls, class_name, bases, namespace_copy)


# Leave code below as is; focus on fixing the metaclass

class ExampleClass(metaclass=AnnouncerMeta):
    """
    Just example of class using AnnouncerMeta class.
    """

    def foo(self, n):
        return f"foo{n}"

    def bar(self, n):
        return f"bar{n}"


test_name = sys.stdin.readline().strip()
if test_name == "sample_test":
    instance = ExampleClass()
    print(instance.foo(1) + instance.bar(2))
