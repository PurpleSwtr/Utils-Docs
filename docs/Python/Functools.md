## Cвернуть последовательность в одно значение, последовательно применяя к элементам какую-то операцию

```
from functools import reduce

numbers = [1, 2, 3, 4, 5]

def multiply(acc, current):
    return acc * current

result = reduce(multiply, numbers)
print(result)
```
