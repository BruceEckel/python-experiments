from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Primes Demo',
    ext_modules=cythonize("primes.pyx", annotate=True),
    zip_safe=False,
)
