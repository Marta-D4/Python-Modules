#!/usr/bin/env python3

def fibonacci_seq(num):
    x, y = 0, 1
    for _ in range(num):
        yield x # Generate actual a value
        x, y = y, x + y # Calculate next num of the sequence

def prime_numbers(nbr):
    x = 2
    while nbr:
        is_prime = True

        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                is_prime = False
                break

        if is_prime:
            yield x
            nbr -= 1
        x += 1    

def display_generators():
    print("\n=== Generator Demonstration ===")
    cnt_fib = 10
    cnt_primes = 5

    fib = fibonacci_seq(cnt_fib)
    print(f"Fibonacci sequence (first {cnt_fib}):", end=" ")
    for num in fib:
        print(num, end=" ")
    
    primes = prime_numbers(cnt_primes)
    print(f"Prime numbers (first {cnt_primes}):", end=" ")
    for prime in primes:
        print(prime, end=" ")

display_generators()