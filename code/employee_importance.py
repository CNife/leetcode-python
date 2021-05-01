from collections import deque
from dataclasses import dataclass


@dataclass
class Employee:
    id: int
    importance: int
    subordinates: list[int]


def get_importance(employees: list[Employee], person_id: int) -> int:
    mapping: dict[int, Employee] = {}
    for employee in employees:
        mapping[employee.id] = employee

    queue: deque[Employee] = deque()
    queue.append(mapping[person_id])
    result = 0
    while len(queue) > 0:
        employee = queue.popleft()
        result += employee.importance
        for subordinate in employee.subordinates:
            queue.append(mapping[subordinate])

    return result


if __name__ == "__main__":
    assert (
            get_importance(
                [
                    Employee(1, 5, [2, 3]),
                    Employee(2, 3, []),
                    Employee(3, 3, []),
                ],
                1,
            )
            == 11
    )
