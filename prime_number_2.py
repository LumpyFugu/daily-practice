def is_prime_optimized(n):
    """
    Features: Only check up to square root, skip even numbers
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):  # Only check odd numbers
        if n % i == 0:
            return False
    return True


def find_primes_optimized(limit):
    """Find all prime numbers <= limit (optimized method)"""
    if limit < 2:
        return []
    
    primes = [2]
    for num in range(3, limit + 1, 2):  # Only check odd numbers
        if is_prime_optimized(num):
            primes.append(num)
    return primes
