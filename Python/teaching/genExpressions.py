import sys
sys.set_int_max_str_digits(0)

# def squares(length):
#     for n in range(length):
#         yield n ** 2

# for square in squares(10):
#     print(square)

def fibonnaci(length):
    a, b = 0, 1
    for n in range(length):
        yield a
        a, b = b, a + b

for k,fib in enumerate(fibonnaci(10000000000)):
    if k%10 == 2:
        print(f"Is the {k}nd value of the Fibonacci sequence: {fib}, even?: {'Yes' if fib % 2 == 0 else 'No'}")
    elif k%10 == 3:
        print(f"Is the {k}rd value of the Fibonacci sequence: {fib}, even?: {'Yes' if fib % 2 == 0 else 'No'}")
    else:
        print(f"Is the {k}th value of the Fibonacci sequence: {fib}, even?: {'Yes' if fib % 2 == 0 else 'No'}")
        
        
        
