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
                uncompleted.append(task)
            else:
                completed.append(task)
        return [uncompleted, completed]

    @staticmethod
    def paste_table_to_file(data: list, filepath: Path):
        md_table = tabulate(
            data, headers=["Текущие задачи", "Выполнено"], tablefmt="github"
        )
        with open(file=filepath, mode="w", encoding="utf-8") as file:
            file.write(md_table)

    @staticmethod
    def paste_list_to_file(completed: list, uncompleted: list, filepath: Path):
        with open(file=filepath, mode="w", encoding="utf-8") as file:
            file.write("\n## Реализовано\n\n")
            file.writelines(line + "\n" for line in completed)
            file.write("\n## Текущие задачи\n\n")
            file.writelines(line + "\n" for line in uncompleted)

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

    def create_mk_checkbox_list(
        self,
    ):
        try:
            input_file = config.TODO_MD
            output_file = config.DOCS_TODO_PATH
            res = self.parser(input_file)
            uncompleted, completed = self.sorting_tasks(res)
            self.paste_list_to_file(
                uncompleted=uncompleted, completed=completed, filepath=output_file
            )
            self.logger.info(
                f"{self.__module__}: список из {input_file.name} добавлен в {output_file.name}"
            )
        except Exception as e:
            self.logger.error(e)


def precommit_generate():
    service = TableGeneratorService()
    service.create_mk_checkbox_list()


if __name__ == "__main__":
    precommit_generate()
