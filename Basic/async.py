import sys

from functools import wraps
from threading import Event, Thread


def async(func):
    @wraps(func)
    def async_closure(*args, **kwargs):
        return _Async(func)(*args, **kwargs)
    return async_closure


class _Async(object):
    """
    Description: Enables multithreading

    Owner: Matt

    Usage:
    task = [async(some_funct_1)(funct_1_parameters), async(some_funct_2)(funct_2_parameters)]
    for t in task:
      t.await()
    """


    class _CaughtException(object):
        def __init__(self, info):
            self.exception_info = info
            self.exc_type = info[0]
            self.exc_value = info[1]
            self.exc_trace = info[2]

    def __init__(self, func):
        self.func = func
        self.event = Event()
        self.__result = None

    def await(self, timeout=None):
        timeout_result = self.event.wait(timeout)
        if isinstance(self.__result, _Async._CaughtException):
            raise self.__result.exc_type, self.__result.exc_value, self.__result.exc_trace
        return timeout_result

    def __call__(self, *args, **kwargs):
        t = Thread(target=self._thread_operation, args=args, kwargs=kwargs)
        self.event.clear()
        t.start()
        return self

    def _thread_operation(self, *args, **kwargs):
        try:
            self.result = self.func(*args, **kwargs)
        except Exception as e:
            self.result = _Async._CaughtException(sys.exc_info())
        finally:
            self.event.set()

    @property
    def result(self):
        self.await()
        return self.__result

    @result.setter
    def result(self, result):
        self.__result = result


