from typing import Final, TextIO


def get_file_contents(file_name: str) -> list[str]:
    FILE_POINTER: Final[TextIO] = open(file_name)
    FILE_CONTENTS: Final[list[str]] = FILE_POINTER.readlines()
    FILE_POINTER.close()

        # newlines at end of strings messes with data comparision so they are removed
    return list[str](map(lambda x: x.rstrip(), FILE_CONTENTS))