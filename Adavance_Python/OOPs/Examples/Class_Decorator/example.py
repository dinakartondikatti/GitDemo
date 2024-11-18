#  class decorator

class Decorator(object):

    def __init__(self, func):
        self.function =func

    def __call__(self, a, b):
        result = self.function(a,b)
        return result*result

@Decorator
def add(a, b):
    return a+b

print(add(2,1))

