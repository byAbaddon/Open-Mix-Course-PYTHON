n = int(input())


def print_line(start, end):
    [print(i, end=" ") for i in range(start, end + 1)]
    print()


[print_line(1, i) for i in range(1, n)]
print_line(1, n)
[print_line(1, i) for i in range(n - 1, 0, -1)]
