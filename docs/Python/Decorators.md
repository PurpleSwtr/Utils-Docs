
## Пример декоратора

```python
from functools import wraps
from typing import Callable

def exmple(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ...
        
        res = func(*args, **kwargs)
        
        return res
    
    return wrapper
```
