import re
from typing import Callable, Generator

# TASK 1
def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 0: return 0
        if n == 1: return 1
        if n in cache: return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

# TASK 2
def generator_numbers(text: str) -> Generator:
    # regexp для пошуку дійсних чисел, відокремлених пробілами
    # " " - звичайний пробіл перед числом
    # \d+ - одна або більше цифр
    # (?:\.\d+)? - необов'язкова десяткова частина
    # " " - звичайний пробіл після числа
    pattern = r' (\d+(?:\.\d+)?) '

    for match in re.finditer(pattern, text):
        yield float(match.group(1))


def sum_profit(text: str, func: Callable[[str], Generator]) -> float:
    return sum(func(text))
