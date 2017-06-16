
## Installation

```
$ pip install git+https://github.com/lavi06/python-cprofile-middleware.git
```

python-cprofile-middleware
==========================

 **Motivation:** To provide an easy to use cProfile middleware to find bottlenecks in code.            

In your settings add:

```python_cprofile_middleware.middleware.ProfilerMiddleware``` to the end your ```MIDDLEWARE_CLASSES``` and 
```python_cprofile_middleware``` to your ```INSTALLED_APPS```
 

For example:

```
if DEBUG:
  MIDDLEWARE_CLASSES += ( 
  'python_cprofile_middleware.middleware.ProfilerMiddleware',
  						)
  INSTALLED_APPS += (
  'python_cprofile_middleware',
  )
```

And that's it, profiling results will be printed on the console

## Decorator

I have also added a decorator in the package which can be used optionally according to one's requirement.

**Motivation:** In case API takes very less time say 10 ms to execute, it is difficult to know which finction is taking the maximum time, as, even the slowest one may take just 1 ms or even less . 
So this decorator provides you option to run the whole code multiple times and thus scaling the total time to a more indicative value.

**How To Use**

In your views.py file add :

```
from python_cprofile_middleware.decorator import my_decorator
```

and at the function you want to run multiple time add decorator:
```
@my_decorator( *no. of times you want it to run )
```


Email me with any questions: [hggoyal06@gmail.com](hggoyal06@gmail.com).

