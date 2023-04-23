def is_simple(n: int) -> bool:
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


n = int(input("Enter a natural number: "))
print(is_simple(n))
