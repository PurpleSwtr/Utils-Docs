from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.docs.router import router as docs_router
from api.settings.router import router as settings_router
from api.sync.router import router as sync_router

app = FastAPI(
    title="MkDocs-Utils",
    root_path="/api/v1",
)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(docs_router)
app.include_router(sync_router)
app.include_router(settings_router)
