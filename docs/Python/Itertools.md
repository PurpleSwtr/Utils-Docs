## Объединение нескольких списков в один

```
from itertools import chain

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

result = list(chain(list1, list2, list3))
print(result) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Разбить список на подсписки

```None
from itertools import batched

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
chunks = list(batched(my_list, 3))
print(chunks)
# [(1, 2, 3), (4, 5, 6), (7, 8)]

```
