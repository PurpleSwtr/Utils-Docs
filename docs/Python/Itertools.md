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

## Объединить списки поэлементно

```python
from itertools import zip_longest

A = ['a', 'b', 'c']
B = [1, 2]

result = list(zip_longest(spisok_A, spisok_B, fillvalue=''))
print(result)
# [('a', 1), ('b', 2), ('c', '')]

```
