class CQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def append_tail(self, value: int) -> None:
        self.input_stack.append(value)

    def delete_head(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop() if self.output_stack else -1


if __name__ == "__main__":
    q1 = CQueue()
    q1.append_tail(3)
    assert q1.delete_head() == 3
    assert q1.delete_head() == -1

    q2 = CQueue()
    assert q2.delete_head() == -1
    q2.append_tail(5)
    q2.append_tail(2)
    assert q2.delete_head() == 5
    assert q2.delete_head() == 2
