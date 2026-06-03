## Найти разницу в двух списках с помощью преобразования в сет

```python
set1 = set([1,2])
set2 = set([1,2,3])
difference = list(set1 - set2) + list(set2 - set1)
```

## Плоский список

```python
nested = [[1, 2], [3, 4], [5]]
flat = [item for sublist in nested for item in sublist]
# Результат: [1, 2, 3, 4, 5]

```
