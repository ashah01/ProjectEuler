for _ in range(int(input())):
    n = int(input().strip()) - 1
    three, five, fifteen = map(lambda m: ((c := n // m) + c * c) * m // 2, (3, 5, 15))
    print(three + five - fifteen)