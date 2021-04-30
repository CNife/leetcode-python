from typing import TypeVar


T = TypeVar("T")


def sorted_list(src: list[T], **kwargs) -> list[T]:
    """
    排序列表，并返回排序后的列表。

    :param src: 要排序的列表
    :param kwargs: 传递给 sort 的参数
    :return: 排序后的列表
    """
    src.sort(**kwargs)
    return src


def sorted_2d_list(src: list[list[T]], **kwargs) -> list[list[T]]:
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
    :return: 两个列表是否相等
    """
    lhs.sort(*args, **kwargs)
    rhs.sort(*args, **kwargs)
    return lhs == rhs


def sorted_2d_equals(lhs: list[list[T]], rhs: list[list[T]], *args, **kwargs) -> bool:
    """
    按每行分别排序、排列每行后的顺序，比较两个二维列表是否相等。

    :param lhs: 二维列表
    :param rhs: 二维列表
    :param args: list.sort 方法参数
    :param kwargs: list.sort 方法参数
    :return: 两个列表是否相等
    """
    if len(lhs) != len(rhs):
        return False
    for i in range(len(lhs)):
        lhs[i].sort(*args, **kwargs)
        rhs[i].sort(*args, **kwargs)
    lhs.sort(*args, **kwargs)
    rhs.sort(*args, **kwargs)
    return lhs == rhs
