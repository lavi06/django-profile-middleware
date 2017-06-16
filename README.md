
## Installation
==========================
```
$ pip install git+https://github.com/lavi06/python-cprofile-middleware.git
```

## Middleware

 **Motivation:** To provide an easy to use cProfile middleware to find bottlenecks in code.            

**How To Use**
(after installation)
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

Profiling results will be printed on the console and will also be saved in a ```profiling_results.txt``` file**.
** ** profiling_results.txt file will be created if not present but if it is there it will update any existing file with same name, 
   So make sure to copy the file somewhere else or rename it in case you want the results later.**


## Decorator

I have also added a decorator in the package which can be used optionally according to one's requirement.

**Motivation:** In case API takes very less time say 10 ms to execute, it is difficult to know which function is taking the maximum time, as, even the slowest one may take just 1 ms or even less . 
So this decorator provides you an option to run the whole code multiple times and thus scaling the total time to a more indicative value.

**How To Use**
(after installation)
In your views.py file add :

```
from python_cprofile_middleware.decorator import my_decorator
```

and at the function you want to run multiple time add decorator:
```
@my_decorator( *no. of times you want it to run )
```


Email me with any questions: [hggoyal06@gmail.com](hggoyal06@gmail.com).

