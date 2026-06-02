from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.docs.router import router as docs_router

app = FastAPI(
    title="Technology-Snippets",
    root_path="/api/v1",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(docs_router)
