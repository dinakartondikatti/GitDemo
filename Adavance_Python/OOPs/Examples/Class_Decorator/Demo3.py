
class Decorator(object):

    def __init__(self, func):
        self.function = func


    def __call__(self, *args,):
        try:
            if any([isinstance(i ,str) for i in args]):
                raise TypeError("Cannot pass string as argument")
            else:
                return self.function(*args)
        except Exception as obj:
            return objcd


@Decorator
def add(*args):
     sum1 =0
     for num in args:
         sum1 = sum1+num
     return sum1

print(add(10, 20 , 30))
print(add(10, '20', 30))


