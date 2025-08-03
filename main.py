n = int(input())

for mask in range(2**n):
    print('{', end='')
    has_before = False
    for i in range(n):
        if mask & (2**i):
            if has_before:
                print(', ', end='')
            print(i + 1, end='')
            has_before = True
    print('}')
