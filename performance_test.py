"""Perfomance Test of Python vs Cython vs Numba library"""
from timeit import timeit

iterations = 1000


cy = timeit("""cython_primes.calculate_primes(1000)""",setup='import cython_primes', number=iterations)
py = timeit("""python_primes.calculate_primes(1000)""",setup='import python_primes', number=iterations)
numba = timeit("""numba_python_primes.jitted_calculate_primes(1000)""",setup='import numba_python_primes', number=iterations)


print(f"Python: {py}s")
print(f"Numba: {numba}s")
print(f"Cython: {cy}s\n")

if py > numba:
    print(f"Numba is {py/numba}x faster")
if py > cy:
    print(f"Cython is {py/cy}x faster")