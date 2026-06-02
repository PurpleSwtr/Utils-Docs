from pathlib import Path

from pydantic_settings import BaseSettings

ROOT = Path(__file__).resolve().parent.parent


class Config(BaseSettings):
    app_name: str = "Utils-Docs"
    DOCS: Path = ROOT / "docs"


config = Config()
