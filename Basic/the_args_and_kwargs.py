# works in Python 3.6 but not Anaconda3 for some reason

import os
import sys

# Example #1
def f(*f_args, **f_kwargs):

    print("f_args are: {}". format(f_args))
    print("f_kwargs are: {}".format(f_kwargs))


zika = 4
mika = range(5)
foo = [1, 2, 3, 4]
gee = {'1': 'one', '2': 'two'}
f('pera', mika, foo, gee, zika='z-i-k-a')


# Example #2
# Python program to illustrate
# *args
def test(arg1, *argv):
    print("first argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


test('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def hello(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" %(key, value))

hello(name="GeeksforGeeks", pera='pera_string')