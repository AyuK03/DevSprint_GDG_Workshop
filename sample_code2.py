def print_fibonacci(n):
    t1, t2 = 0, 1
    print("Fibonacci Sequence:", end=" ")
    for _ in range(n):
        print(t1, end=" ")
        t1, t2 = t2, t1 + t2
    print()

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print_fibonacci(n)
