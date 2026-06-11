
## Уровни логов

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Отладочная информация")
logging.info("Программа запущена")
logging.warning("Это предупреждение")
logging.error("Произошла ошибка")
logging.critical("Критическая ошибка")
```

## Использование логгера в модулях

```python
import logging

logger = logging.getLogger(__name__)

```

## Запись логов в файл

```python
import logging

logging.basicConfig(
    filename='app.log', 
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
```
