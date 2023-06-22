import cython
import math

def cpu_intensive(n: cython.ulong, multiplier: cython.ulong) -> cython.double:
    result: cython.double = 0.0
    i: cython.ulong

    for i in range(10_000_000 * multiplier):
        result += math.sqrt(i**3 + i**2 + i * n)

    return result

# The above compiles and runs but produces incorrect results, and is about 10x slower than the Rust extension.
# I also tried the following, which compiles but produces "math domain" errors at runtime:

# import math
#
# cpdef double cpu_intensive(long long n, long long multiplier):
#    cdef double result = 0.0
#    cdef long long i
#
#    for i in range(10_000_000 * multiplier):
#        result += math.sqrt(i**3 + i**2 + i * n)
#
#    return result

# And I tried this, which produces a lot of `nan`s:

# cimport cython
# from libc.math cimport sqrt

# @cython.boundscheck(False)
# @cython.wraparound(False)
# def cpu_intensive(long long n, long long multiplier) -> double:
#     cdef double result = 0.0
#     cdef long long i
#     cdef long long argument

#     for i in range(10_000_000 * multiplier):
#         argument = i**3 + i**2 + i * n
#         result += sqrt(argument)

#     return result
