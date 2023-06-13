# Exploring ProcessPoolExecutor

Python's `ProcessPoolExecutor` uses simple syntax to distribute tasks across multiple *processes* on your machine.
In `go.py`, look at this expression:
```python
executor.map(cpu_intensive, range(tasks), [multiplier] * tasks)
```
This starts `tasks` new processes. 
Each new process contains a function call to `cpu_intensive` for its corresponding set of arguments from `range(tasks)` and `[multiplier] * tasks`
(`map` effectively `zip`s the two sequences to produce a sequence of argument lists).

When you run the program, first open up your task manager and configure it to show the individual cores (in Windows, right-click in the CPU graph).
You will see that the usage of every core is maximized while the calculations are performed.

The program is written so you can play with different values, such as the number of tasks, and see the results.

## Rust Extension

The `rust_extension` subdirectory contains a python extension written in Rust using the `Py03` library. 
You must be in a virtual environment to both build and use the extension (I used `hatch shell`).
The extension is used in the `using_rust_extension.py` script. 
Note that the only difference between this and the `with_concurrency.py` script is that the `cpu_intensive()` function is now imported from a module.

## Rust

In the `rust` subdirectory you'll find the equivalent program but using Rust for everything.

Note: The Rust program uses channels (the code is cleaner) and thus does not collect the results in order.

By looking at the task manager, you can see how the threads are allocated across cores. 
Thus the Rust program is running within a single process that makes full use of all cores. 
Because it is in a single process---unlike the Python program, which distributes each call to `cpu_intensive()` into its own process---the Rust program does not have the overhead of inter-process communication (IPC). 
(In this example there's virtually no IPC involved so we do not see an impact from it).

## Performance Results

Output from running `compare_all.bat` on my Windows 11 desktop machine.
Note that the virtual environment was started inside the `rust-extension` directory, and all Rust programs have been built using `--release`:

```text
(rust-extension) PS C:\git\python-experiments\fully_loaded> .\compare_all.bat

C:\git\python-experiments\fully_loaded>python no_concurrency.py
logical_processors = 32
tasks = 32
[1.264911011363067e+17, 1.2649110113631182e+17, 1.2649110113631494e+17, 1.2649110113631802e+17, 1.2649110113632114e+17, 
1.2649110113632403e+17, 1.2649110113632698e+17, 1.2649110113632997e+17, 1.26491101136333e+17, 1.2649110113633622e+17, 
1.2649110113633933e+17, 1.2649110113634237e+17, 1.264911011363455e+17, 1.2649110113634862e+17, 1.2649110113635166e+17, 
1.264911011363548e+17, 1.2649110113635794e+17, 1.2649110113636128e+17, 1.2649110113636429e+17, 1.2649110113636734e+17, 
1.264911011363705e+17, 1.2649110113637357e+17, 1.2649110113637662e+17, 1.2649110113637963e+17, 1.2649110113638283e+17, 
1.2649110113638595e+17, 1.264911011363889e+17, 1.2649110113639203e+17, 1.264911011363954e+17, 1.2649110113639843e+17, 
1.2649110113640166e+17, 1.264911011364046e+17]
Elapsed time: 43.73s

C:\git\python-experiments\fully_loaded>python with_concurrency.py
logical_processors = 32
tasks = 32
[1.264911011363067e+17, 1.2649110113631182e+17, 1.2649110113631494e+17, 1.2649110113631802e+17, 1.2649110113632114e+17, 
1.2649110113632403e+17, 1.2649110113632698e+17, 1.2649110113632997e+17, 1.26491101136333e+17, 1.2649110113633622e+17, 
1.2649110113633933e+17, 1.2649110113634237e+17, 1.264911011363455e+17, 1.2649110113634862e+17, 1.2649110113635166e+17, 
1.264911011363548e+17, 1.2649110113635794e+17, 1.2649110113636128e+17, 1.2649110113636429e+17, 1.2649110113636734e+17, 
1.264911011363705e+17, 1.2649110113637357e+17, 1.2649110113637662e+17, 1.2649110113637963e+17, 1.2649110113638283e+17, 
1.2649110113638595e+17, 1.264911011363889e+17, 1.2649110113639203e+17, 1.264911011363954e+17, 1.2649110113639843e+17, 
1.2649110113640166e+17, 1.264911011364046e+17]
Elapsed time: 5.52s

C:\git\python-experiments\fully_loaded>python using_rust_extension.py
logical_processors = 32
tasks = 32
[1.264911011363067e+17, 1.2649110113631182e+17, 1.2649110113631494e+17, 1.2649110113631802e+17, 1.2649110113632114e+17, 
1.2649110113632403e+17, 1.2649110113632698e+17, 1.2649110113632997e+17, 1.26491101136333e+17, 1.2649110113633622e+17, 
1.2649110113633933e+17, 1.2649110113634237e+17, 1.264911011363455e+17, 1.2649110113634862e+17, 1.2649110113635166e+17, 
1.264911011363548e+17, 1.2649110113635794e+17, 1.2649110113636128e+17, 1.2649110113636429e+17, 1.2649110113636734e+17, 
1.264911011363705e+17, 1.2649110113637357e+17, 1.2649110113637662e+17, 1.2649110113637963e+17, 1.2649110113638283e+17, 
1.2649110113638595e+17, 1.264911011363889e+17, 1.2649110113639203e+17, 1.264911011363954e+17, 1.2649110113639843e+17, 
1.2649110113640166e+17, 1.264911011364046e+17]
Elapsed time: 0.31s

C:\git\python-experiments\fully_loaded>.\rust\target\release\rust.exe
[src\main.rs:16] logical_processors = 32
[src\main.rs:18] tasks = 32
1.2649110113631182e17
1.2649110113631494e17
1.2649110113632698e17
1.264911011363067e17
1.2649110113631802e17
1.2649110113632997e17
1.2649110113633622e17
1.26491101136333e17
1.2649110113639203e17
1.264911011364046e17
1.2649110113639843e17
1.2649110113638283e17
1.2649110113637963e17
1.2649110113640166e17
1.2649110113637662e17
1.264911011363889e17
1.2649110113635166e17
1.2649110113632403e17
1.2649110113633933e17
1.2649110113636734e17
1.264911011363954e17
1.264911011363455e17
1.264911011363705e17
1.2649110113634862e17
1.2649110113632114e17
1.2649110113634237e17
1.2649110113636429e17
1.264911011363548e17
1.2649110113635794e17
1.2649110113637357e17
1.2649110113638595e17
1.2649110113636128e17
Elapsed time: 0.11s
```
