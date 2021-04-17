from typing import Callable, List, Tuple, TypeVar

from rich.console import Console
from rich.panel import Panel

console = Console()


def test(
        function: Callable,
        test_cases: List[Tuple],
        *,
        args_func: Callable = None,
        expect_func: Callable = None,
        actual_func: Callable = None,
        map_func: Callable = None,
        equals_func: Callable = None,
) -> None:
    """
    使用测例测试函数。
    test_case 中的测例，每项都要按照 function 的参数 + 希望得到的结果来组成元组。

    :param function: 要测试的函数
    :param test_cases: 测例
    :param args_func: 从 test_cases 中取得 function 参数的函数
    :param expect_func: 从 test_cases 中取得希望得到的结果的函数
    :param actual_func: 从 test_cases 和 function 运行结果中取得实际结果的函数
    :param map_func: 将 function 运行结果和希望得到的结果做映射的函数
    :param equals_func: 判断运行结果和希望结果是否相等的函数
    """
    if args_func is None:
        def args_func(case):
            return case[:-1]

    if expect_func is None:
        def expect_func(case):
            return case[-1]

    if actual_func is None:
        def actual_func(_, prev_actual):
            return prev_actual

    if map_func is None:
        def map_func(item):
            return item

    if equals_func is None:
        def equals_func(lhs, rhs):
            return lhs == rhs

    for test_case in test_cases:
        args = args_func(test_case)
        expect = expect_func(test_case)
        actual = actual_func(test_case, function(*args))

        expect, actual = map_func(expect), map_func(actual)
        passed = equals_func(actual, expect)

        if not passed:
            console.print(f"Test for [blue]{function}[/] [red]Failed[/]!")
            console.print(Panel(str(args), title="args"))
            console.print(Panel(str(expect), title="expect"))
            console.print(Panel(str(actual), title="actual"))
            exit(1)

    console.print(f"Test for [blue]{function}[/] [green]Succeed[/]!")


T = TypeVar("T")


def sorted_list(src: List[T], **kwargs) -> List[T]:
    """
    排序列表，并返回排序后的列表。

    :param src: 要排序的列表
    :param kwargs: 传递给 sort 的参数
    :return: 排序后的列表
    """
    src.sort(**kwargs)
    return src


def sorted_2d_list(src: List[List[T]], **kwargs) -> List[List[T]]:
    """
    排序并返回二维列表。

    :param src: 要排序的二维列表
    :param kwargs: 传递给 sort 的参数
    :return: 排序后的二维列表
    """
    for ll in src:
        ll.sort()
    src.sort(**kwargs)
    return src


def sorted_equals(lhs: list[T], rhs: list[T], *args, **kwargs) -> bool:
    """
    按排序后的顺序，比较两个列表是否相等。

    :param lhs: 列表
    :param rhs: 列表
    :param args: list.sort 方法参数
    :param kwargs: list.sort 方法参数
    :return:
    """
    lhs.sort(*args, **kwargs)
    rhs.sort(*args, **kwargs)
    return lhs == rhs
