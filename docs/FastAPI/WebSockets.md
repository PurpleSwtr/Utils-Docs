## Простейшая реализация веб-сокета

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket("/ws")
async def ws(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            msg = await ws.receive_text()
            await ws.send_text(f"эхо: {msg}")
    except WebSocketDisconnect:
        pass
```