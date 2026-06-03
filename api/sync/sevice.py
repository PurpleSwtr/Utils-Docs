import asyncio
import os
import subprocess

from api.core.config import config


class SyncService:
    def __init__(self):
        self.repo_path = config.DOCS.parent.parent
        pass

    def _sync_execute_cmd(self, program: str, args: list[str]) -> str:
        if not os.path.exists(self.repo_path):
            raise FileNotFoundError(f"директория не найдена: {self.repo_path}")

        result = subprocess.run(
            [program, *args],
            cwd=self.repo_path,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

        if result.returncode != 0:
            error_msg = result.stderr.strip() or result.stdout.strip()
            raise RuntimeError(f"{error_msg}")

        return result.stdout.strip()

    async def run_cmd(self, program: str, args: list[str]) -> str:
        return await asyncio.to_thread(self._sync_execute_cmd, program, args)

    async def sync_github(self, msg: str):
        try:
            await self.run_cmd("git", ["add", "docs"])
            await self.run_cmd("git", ["commit", "--no-verify", "-m", msg])
            await self.run_cmd("git", ["push"])

        except RuntimeError as e:
            if "nothing to commit" in str(e) or "no changes added to commit" in str(e):
                return
            print(f"{e}")
            raise

    async def sync_run(self, msg: str):
        await self.sync_github(msg)
