from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parent.parent.parent


class Config(BaseSettings):
    app_name: str = "Utils-Docs"

    DOCS: Path = ROOT / "docs"

    ASSETS_PATH: Path = DOCS / "assets"
    IMAGES_PATH: Path = ASSETS_PATH / "images"
    GIFS_PATH: Path = ASSETS_PATH / "gifs"
    allowed_extensions: set = {".jpg", ".jpeg", ".png", ".gif"}

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
