def do_it(param_1 : int, param_2 : str, param_3 : float) -> float:
    """
    Эта функция берет первые два параметра, складывает их и делит на третий.
    Результат печатается в консоль.
    Параметры должны быть в консоли.
    """
    result = (param_1 + param_2) * param_3
    return [param_1, param_2, param_3, result]


lst = do_it(1, 2, 3)


# int — 19
# float — 2.6
# bool — True/False
# str — “Test”
# dict — {}
# list — []