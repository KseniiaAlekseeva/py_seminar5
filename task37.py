def revers(n: int) -> None:
    if n == 0:
        return print('')
    k = input()
    revers(n-1)
    return print(k)


n = int(input("Enter a natural N: "))
revers(n)
