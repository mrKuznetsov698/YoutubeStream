from typing import Union, Tuple


# return error, mode, x, y
def parse_string(txt: str) -> Union[Tuple[int, int, int]]:
    error, x, y = 0, 0, 0
    try:
        x, y = [int(i) for i in txt.split(' ', 2)]
    except Exception:
        error = 1
    return error, x, y
