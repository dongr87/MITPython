# Introduction to Computer Science and Programming Using Python

## Lecture 9 Complexity
###Measuring complexity
- How much time will it take a program to run?
- How muc memory will it need to run?
we need to balance minimizing computational complexity with conceptual complexity.(Keep code simple)
####Speed depends on:
1. speed of computer
2. specifics of Python implementation
3. Value of input

#### avoid 1 and 2 by measuring time in terms of number of basic steps executed
use a __random access machine(RAM)__
Which means counting steps of the function.
#### For the 3 point, measure time in terms of size of input

__point 1) and 2)__
_eg. linear search_ode is to check if it works in browser,
if not, I'll use another method.
*/
function getElementsByClassName(node, classname) {
  if(node.getElementsByClassName) {
    //use the current method
    return node.getElementsByClassName(classname);
  }
  else {
    var results = new Array();
    var elems = node.getElementsByTagName("*");
    for (var i = 0; i < elems.length; i++) {
      if (elems[i].className.indexOf(classname) != -1) {
        results[results.length] = elems[i];
      }
    }
    return results;
  }


## Lecture 11 Classes
### Objects
#### Introduction of Objects
Everything in Python is an __object__ and has a __type__.

__classes__ are _user-defined objects.

Objects have:
- A type (a particular object is said to be an __instance__ of a type)
- An internal data representation (primitive or composite)
 + internal presentation should be private
- A set of procedures for interaction w/ the object

Objects are a data abstraction that encapsulate:
- internal representation
- __interface__ for interacting with object

_Object_ should be able to:
- create an _instance_
- destroy objects
    + explicityly using _del_ or just _forget_ about them
    + python system will reclaim destroyed or inaccessible objects, called _garbage collection_

#### Create an Object
- using ```class``` to create a class 
- using ``` __init__ ``` method to create an object
- using ```__str__``` method to print the object
- using ```isinstance()``` method to check what type an object is

###### example of a class
```python
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<"+self.x+","self.y+">"

c = Coordinate(3,4)
isinstance(c,Coordinate) #c is the instance, Coordinate is the type. Return a Boolean whether c is an instance of Coordinate

```


