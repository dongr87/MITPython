
### 2.4-Map/Reduce
### 2.6-Callable Functions
Define a function to call the real functional function. Also called __Closure__.  
When we call the function, every time we call a new functional function. So f1 != f2  
__Never use loop in Closure__  
If a loop is a _must_ in Closure, we should define another function and call the function inside the loop.

### Anonymous Function (lambda)
### 2.7-Decorator
### Partial Function
Fix some arguments of the function to make it easier to call.  
eg. 
``` python
import functools
int(x, base=2)
int2 = functools.partial(int, base=2)
```
You can still call _'base'_ variable with other value.

## OOP
### Module
__Package__ must have __\_\_init\_\___ file.  
Encapsulation  
- Private Variable (\_\_variableName)
- Inheritence and Polymophism
- Java (static language) __vs__ Python (dynamic language)
- 3.1-Obtain object's information
 + type()
 + isinstance()
 + dir()
- Instance attr vs Class attr
 + Python is dynamic language, you can bind attributes to instance based on class anytime.
 + Instance attr will override the Class attr until it's deleted
- 3.2-\_\_slots\_\_ method
- 3.3-@property
- multiple inheritance  **MixIn**
- 3.4-custom class

