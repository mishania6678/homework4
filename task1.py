from sys import argv


def payroll(money_per_hour: int, hours: int, premium=0) -> int:
    return int(money_per_hour) * int(hours) + int(premium)


print(payroll(int(argv[1]), int(argv[2]), premium=int(argv[3]) if len(argv) == 4 else 0))
