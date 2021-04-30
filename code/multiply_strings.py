def _parse(number_in_string: str) -> list[int]:
    return [ord(digit) - ord("0") for digit in number_in_string]


def _multiply_digit(num_str: list[int], digit: int, offset: int) -> list[int]:
    carriage = 0
    result = [0] * offset
    for num_digit in reversed(num_str):
        product = num_digit * digit + carriage
        result.append(product % 10)
        carriage = product // 10
    if carriage > 0:
        result.append(carriage)
    return result


def multiply(lhs: str, rhs: str) -> str:
    if not lhs or not rhs:
        return ""
    if len(lhs) < len(rhs):
        lhs, rhs = rhs, lhs
    if len(rhs) == 1:
        if rhs == "0":
            return "0"
        if rhs == "1":
            return lhs

    lhs, rhs = _parse(lhs), _parse(rhs)
    lines = [_multiply_digit(lhs, digit, i) for i, digit in enumerate(reversed(rhs))]
    carriage = 0
    result = []
    for i in range(max(len(line) for line in lines)):
        digit_sum = carriage
        for line in lines:
            if i < len(line):
                digit_sum += line[i]
        result.append(str(digit_sum % 10))
        carriage = digit_sum // 10
    if carriage > 0:
        result.append(str(carriage))
    return "".join(reversed(result))


if __name__ == "__main__":
    assert multiply("0", "0") == "0"
    assert multiply("0", "100") == "0"
    assert multiply("100", "0") == "0"
    assert multiply("1", "100") == "100"
    assert multiply("123", "456") == "56088"
