from api.core.config import config


class SettingsService:
    def __init__(self):
        self.repo_path = config.DOCS.parent
        pass

    def get_mkdocs_yml(self):
        mkdocs_yml = self.repo_path / "mkdocs.yml"
        if not mkdocs_yml.exists():
            raise FileNotFoundError(mkdocs_yml)
        with open(file=mkdocs_yml, mode="r", encoding="utf-8") as f:
            return f.read()
