## Найти разницу в двух списках с помощью преобразования в сет

```python
set1 = set([1,2])
set2 = set([1,2,3])
difference = list(set1 - set2) + list(set2 - set1)
```