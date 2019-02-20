import inspect


def calling_stack_decorator(decorated):
    def wraper():
        func_name = inspect.stack()[0][3]
        caller_name = inspect.stack()[1][3]
        print("I'm {}.\n{} called me!".format(func_name,caller_name))
        decorated()

    return wraper

@calling_stack_decorator
def foo():
    pass

def bar(f):
  f()

bar(foo)
# I'm foo.
# bar called m

