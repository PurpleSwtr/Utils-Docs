from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from api.docs.router import router as docs_router
from api.files.router import router as files_router
from api.settings.router import router as settings_router
from api.sync.router import router as sync_router

app = FastAPI(
    title="MkDocs-Utils",
    root_path="/api/v1",
)


@app.get("/", include_in_schema=False)
async def root_redirect():
    return RedirectResponse(url="/docs")


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost",
    "http://127.0.0.1",
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
app.include_router(files_router)
