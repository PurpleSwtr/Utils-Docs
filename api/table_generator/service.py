import logging
from itertools import zip_longest
from pathlib import Path

from tabulate import tabulate

from api.core.config import config


class TableGeneratorService:
    """
    Изначально идея была в том, чтобы представить выполненные и текущие задачи через таблицу на сайте.
    Сейчас я всё таки думаю представить это в виде обычного отсортированного списка.
    """

    def __init__(
        self,
    ):
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def parser(filename: Path):
        result = []
        with open(file=filename, mode="r", encoding="utf-8") as f:
            for line in f:
                if "- [ ]" in line or "- [x]" in line:
                    result.append(line.strip())
        return result

    @staticmethod
    def sorting_tasks(tasks: list) -> list[list]:
        completed, uncompleted = [], []
        for task in tasks:
            if "[ ]" in task:
                uncompleted.append(task.replace("- [ ] ", ""))
            else:
                completed.append(task.replace("- [x] ", ""))
        return [uncompleted, completed]

    @staticmethod
    def paste_table_to_file(data: list, filepath: Path):
        md_table = tabulate(
            data, headers=["Текущие задачи", "Выполено"], tablefmt="github"
        )
        with open(file=filepath, mode="w", encoding="utf-8") as file:
            file.write(md_table)

    def create_md_table(
        self,
    ):
        try:
            input_file = config.TODO_MD
            output_file = config.DOCS_TODO_PATH
            res = self.parser(input_file)
            uncompleted, completed = self.sorting_tasks(res)

            result_table = []

            for u_task, c_task in zip_longest(uncompleted, completed, fillvalue=""):
                if u_task or c_task:
                    result_table.append([u_task, c_task])

            self.paste_table_to_file(data=result_table, filepath=output_file)
            self.logger.info(
                f"{self.__module__}: таблица из {input_file.name} добавлена в {output_file.name}"
            )
        except Exception as e:
            self.logger.error(e)
