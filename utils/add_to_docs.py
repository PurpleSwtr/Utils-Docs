def add_to_docs(tittle: str, text: str, lang: str, is_code: bool = True):
    return (
        f"## {tittle}\n\n```{lang}\n{text}\n```\n"
        if is_code
        else f"## {tittle}\n\n{text}\n\n"
    )


print(repr(add_to_docs("Заметочка", "Кодик\nкодик", "python", False)))
