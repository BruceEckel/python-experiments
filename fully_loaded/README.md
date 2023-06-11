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

On my Windows 11 desktop machine, the program as-is completes in 5.6 seconds, using 32 tasks (logical_processors).

## Rust

In the `rust` subdirectory you'll find the equivalent program using the `tokio` library. This runs about ten times faster.

Note: The Rust program uses channels (the code is cleaner) and thus does not collect the results in order.
