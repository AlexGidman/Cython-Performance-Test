"""Use numba Python library to improve performance of function"""

import numba
from python_primes import calculate_primes

jitted_calculate_primes = numba.njit()(calculate_primes)