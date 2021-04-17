from typing import List


class BrowserHistory:
    def __init__(self, homepage: str):
        self.stack: List[str] = [homepage]
        self.pointer: int = 0

    def visit(self, url: str) -> None:
        if self.pointer < len(self.stack) - 1:
            self.stack[self.pointer + 1] = url
            del self.stack[self.pointer + 2 :]
        else:
            self.stack.append(url)
        self.pointer += 1

    def back(self, steps: int) -> str:
        back_pointer = max(self.pointer - steps, 0)
        self.pointer = back_pointer
        return self.stack[back_pointer]

    def forward(self, steps: int) -> str:
        forward_pointer = min(self.pointer + steps, len(self.stack) - 1)
        self.pointer = forward_pointer
        return self.stack[forward_pointer]


b = BrowserHistory("leetcode.com")
b.visit("google.com")
b.visit("facebook.com")
b.visit("youtube.com")
assert b.back(1) == "facebook.com"
assert b.back(1) == "google.com"
assert b.forward(1) == "facebook.com"
b.visit("linkedin.com")
assert b.forward(2) == "linkedin.com"
assert b.back(2) == "google.com"
assert b.back(7) == "leetcode.com"
