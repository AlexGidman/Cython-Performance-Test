# Cython-Performance-Test
A quick look into Cython. This projects tests a simple prime number range calculation executed in Python and in C using Cython library.

**EDIT**
A performance test using the 'numba' library has been added for reference.

## How to Run:

* Install the requirements:

```bash
pip install -r requirements.txt
```

* Once you have cloned the repository and installed Cython, build the C code:

```bash
python setup.py build_ext --inplace
```

* Then run:

```bash
python3 performance_test.py
```

## Conclusion:

Using Cython runs much faster than Python. However, I did encounter several compilation issues when writing the .pyx file that did not contain much useful traceback information; this could be problematic for more complex programs.

Using the 'numba' library did improve performance, but not as much as Cython. For simple performance improvements in a large Python project, numba may prove sufficient.