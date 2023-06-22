# Cython version of the "fully loaded" example

## NOTE: Incorrect output

Although the Cython extension compiles and the Python program runs, it produces incorrect output:

```text
[436761786922.2004, 436750762281.1235, 436750708961.4686, 436736804516.73987, 
436740765573.11554, 436737440239.4719, 436732793677.42975, 436735919555.46313, 
436741762386.9799, 436748184223.7655, 436751228123.503, 436756720929.215, 
436758359932.42413, 436766135219.74005, 436778508810.5421, 436790075591.25714, 
436794379998.78204, 436795219987.5408, 436785351629.4575, 436794892388.3982, 
436792211078.1118, 436790924878.58594, 436800405286.84674, 436807742521.04285, 
436800659103.7269, 436807249123.5281, 436808685017.141, 436817521078.543, 
436819211761.98413, 436809842746.0968, 436812574790.8651, 436803100033.0286]
```

It is unclear to me so far what is happening here. The `i: cython.ulong` is necessary
to prevent overflow, but it generates a `warning C4018: '<': signed/unsigned mismatch`.

In general the Cython experience is significantly more difficult than Rust.

## Installing and Running

1.  Install Cython and a supporting C compiler as described in:
    https://cython.readthedocs.io/en/latest/src/quickstart/install.html

2.  Build the cython extension using the command:
    ```text
    > python setup.py build_ext --inplace
    ```

3.  Run the program:
    ```text
    > python cython_concurrency.py
    ```
