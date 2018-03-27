# Fibonacci numbers   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# Implment a program that will print a LIST of fibonacci numbers to a specified length.

# Example: fibonacci(10)
# input: number  (desired length of array)
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] - the first 10 numbers of the fibonacci sequence

# Hint:
# You may start your array like this:
# list = [0, 1]


# *** your code here ***
def fibonacci(num):
    fibonacci_list = []
    for i in range(num):
        if i <= 1:
            fibonacci_list.append(i)
        elif i == 2:
            fibonacci_list.append(1)
        else:
            fibonacci_list.append(fibonacci_list[len(fibonacci_list) - 2] + fibonacci_list[len(fibonacci_list) - 1])
    return fibonacci_list

print(fibonacci(20))
