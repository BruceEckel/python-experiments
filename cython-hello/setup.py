from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Integration Demo',
    ext_modules=cythonize("integrate.pyx"),
    zip_safe=False,
)
