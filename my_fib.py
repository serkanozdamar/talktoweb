def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def my_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        x = 1
        y = 1
        my_sum = 0
        for i in range(2, n+1):
            my_sum = x + y
            x = y
            y = my_sum

        return my_sum
# my_result = fib(50)
my_result = my_fib(100)
print(my_result)
