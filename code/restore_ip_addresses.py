def restore_ip_address(src: str) -> list[str]:
    segments, results = [], []

    def is_valid_segment(segment: str) -> bool:
        n = len(segment)
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n == 2:
            return segment[0] != "0"
        elif n == 3:
            if segment[0] == "1":
                return True
            elif segment[0] == "2":
                return segment[1] < "5" or segment[1] == "5" and segment[2] < "6"
        else:
            return False

    def dfs(s: str, dots: int) -> None:
        nonlocal segments, results
        if dots:
            for idx in range(1, min(3, len(src) - dots) + 1):
                segment = s[:idx]
                if is_valid_segment(segment):
                    segments.append(segment)
                    dfs(s[idx:], dots - 1)
                    segments.pop()
        else:
            if is_valid_segment(s):
                segments.append(s)
                results.append(".".join(segments))
                segments.pop()

    dfs(src, 3)
    return results


if __name__ == "__main__":
    assert restore_ip_address("25525511135") == ["255.255.11.135", "255.255.111.35"]
