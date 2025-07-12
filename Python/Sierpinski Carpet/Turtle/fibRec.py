import time
import sys

sys.set_int_max_str_digits(10000000)


def fib(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
def FibonacciMemo(n,memo={0:1,1:1}):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = FibonacciMemo(n-1,memo) + FibonacciMemo(n-2,memo)
        return memo[n]

timeTaken = 0
maxValue = 0
for i in range(0,1000000,100):
    StartTime = time.time()
    maxValue = f"FibonacciMemo({i}) = {FibonacciMemo(i)}"
    timeTaken = time.time() - StartTime
    maxValue = maxValue + f" in {timeTaken} seconds"
    print(maxValue)

print(maxValue)