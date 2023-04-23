def fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return fib(n-1)+fib(n-2)


n = int(input("Enter number n>=0: "))
print(fib(n))
