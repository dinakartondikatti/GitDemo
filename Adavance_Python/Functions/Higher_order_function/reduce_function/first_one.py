# reduce() --> this is built in higher order function defined in functool module.
# syntax -->import functools ,  functools.reduce(function_name , iterable)
# it doesn't return another iterable but returns a single reduced value
import functools

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# def func(a, b):
#     return a + b

reduce_obj = functools.reduce(lambda a,b:a+b , nums)
print(reduce_obj)
