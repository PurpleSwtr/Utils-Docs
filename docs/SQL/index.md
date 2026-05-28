### `CROSS JOIN` – декартово произведение

```sql
SELECT * FROM A CROSS JOIN B;
```

### `FULL JOIN` – все строки из обеих таблиц

```sql
SELECT * FROM A FULL JOIN B ON A.id = B.id;
```

### `BETWEEN` с годами (функция YEAR)

```sql
SELECT * FROM Student WHERE YEAR(birthday) IN (2000, 2002, 2004);
WHERE YEAR(birthday) BETWEEN 2000 AND 2004;
```

### Подзапрос с `IN`

```sql
SELECT * FROM Orders o
WHERE o.IdOrd IN (
    SELECT oi.IdOrd FROM OrdItem oi
    JOIN Product p ON oi.IdProd = p.IdProd
    WHERE p.Description = N'SSD M2 xpg'
);
```

### Очистить таблицу

```sql
TRUNCATE TABLE MyTable;
-- или
DELETE FROM MyTable;
```
