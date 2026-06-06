## **Полезные ссылки**

- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)

## Редирект с главной странички на документацию

```python
@app.get("/", include_in_schema=False)
async def root_redirect():
    return RedirectResponse(url="/docs")
```
