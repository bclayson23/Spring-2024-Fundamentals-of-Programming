# Make a fibonacci sequence

# using rcursions
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


def fibSeries(nterms):
    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence: ")
        for i in range(1, nterms + 1):
            print(recur_fibo(i))


fibSeries(30)
print()


# using loops
def fibonacciSeries(num):
    if num <= 0:
        print("Enter a value greater than zero")
    elif num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    else:
        fib_list = [1, 1]
        for i in range(2, num):
            # return fib_list.extend(fibonacciSeries(fib_list[i-1])+fibonacciSeries(fib_list[i-2]))
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list


print(fibonacciSeries(30))
