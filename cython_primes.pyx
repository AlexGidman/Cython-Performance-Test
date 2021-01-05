cpdef list calculate_primes(int num):
    """Calcuate primes between range of 1 and num"""
    cdef list primes = []
    cdef int x
    cdef int y
    cdef int count
    for x in range(1, (num+1)):
        count = 0
        for y in range(1, (num+1)):
            if count > 2:
                break
            if x % y == 0:
                count += 1
        if count == 2:
            primes.append(x)
    return primes
