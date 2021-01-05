"""Perfomance Test of Python vs Cython"""
from timeit import timeit

iterations = 100


cy = timeit("""cython_primes.calculate_primes(1000)""",setup='import cython_primes', number=iterations)
py = timeit("""python_primes.calculate_primes(1000)""",setup='import python_primes', number=iterations)

print(f"Python: {py}s")
print(f"Cython: {cy}s")

if py > cy:
    print(f"Cython is {py/cy}x faster")