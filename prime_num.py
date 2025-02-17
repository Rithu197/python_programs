def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Find all prime numbers between 1 and 100
prime_numbers = []
for number in range(1, 101):
    if is_prime(number):
        prime_numbers.append(number)

# Calculate the sum of prime numbers
sum_of_primes = sum(prime_numbers)

print("Prime numbers between 1 and 100:", prime_numbers)
print("Sum of prime numbers:", sum_of_primes)
