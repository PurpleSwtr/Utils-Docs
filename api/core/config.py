from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parent.parent


class Config(BaseSettings):
    app_name: str = "Utils-Docs"
    DOCS: Path = ROOT / "docs"
    TOKEN: str = ""
    REPO_OWNER: str = ""
    REPO_NAME: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )


config = Config()
