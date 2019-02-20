import inspect


# def foo():
#     print()

# def bar(f):
#     print( f.__name__ )

# bar(foo)

def calling_stack_decorator(decorated):
    def wraper():
        print( inspect.stack()[0].__dir__() )

        decorated()

    return wraper

@calling_stack_decorator
def foo():
    pass

foo()

