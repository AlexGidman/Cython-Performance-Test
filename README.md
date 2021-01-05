# Cython-Performance-Test
A quick look into Cython. This projects tests a simple prime number range calculation executed in Python and in C using Cython library.

## How to Run:

Once you have cloned the repository and installed Cython, build the C code:

```bash
python setup.py build_ext --inplace
```

Then run:

```bash
python3 performance_test.py
```

## Conclusion:

Using Cython runs much faster than Python. However, I did encounter several compilation issues when writing the .pyx file that did not contain much useful traceback information; this could be problematic for more complex programs.