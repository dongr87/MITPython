import types

def fn():
    pass

# define names for all type symbols known in the standard interpreter
type(fn)==types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType
type((x for x in range(10)))==types.GeneratorType

# return whether an object is of a class or of subclass thereof
isinstance([1, 2, 3], (list, tuple))

# obtain all the methods and attributes of an object
dir('ABC')

# private method
len('ABC')
'ABC'.__len__()

# has attribute
hasattr(obj, 'x')
setattr(object, name, value)
getattr(object, name)

# example
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

