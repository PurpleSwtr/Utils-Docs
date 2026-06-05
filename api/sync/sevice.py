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

    async def sync_github(self, msg: str, target_branch: str = "bot/docs-auto-sync"):
        current_branch_result = await self.run_cmd("git", ["branch", "--show-current"])
        original_branch = current_branch_result.strip() or "main"
        try:
            status = await self.run_cmd("git", ["status", "--porcelain", "docs"])
            if not status.strip():
                return {
                    "status": "success",
                }

            await self.run_cmd("git", ["add", "docs"])
            commit_msg = f"docs: {msg}" if not msg.startswith("docs:") else msg
            await self.run_cmd("git", ["commit", "--no-verify", "-m", commit_msg])
            await self.run_cmd("git", ["switch", "-C", target_branch])

            await self.run_cmd("git", ["push", "-u", "origin", target_branch])

            return {
                "status": "success",
            }

        except Exception as e:
            print(e)
            return {"status": "error", "message": str(e)}

        finally:
            try:
                await self.run_cmd("git", ["switch", original_branch])
            except Exception as rollback_error:
                print(f"{original_branch}: {rollback_error}")

    async def sync_run(self, msg: str):
        await self.sync_github(msg)
