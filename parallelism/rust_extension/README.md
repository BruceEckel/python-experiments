# Building and Running

Follow the instructions in: https://pyo3.rs/v0.19.0/

You must be inside a virtual environment for this to work; I use:
```text
hatch shell
```

To build, run 
```text
maturin develop --release`
```

Run the program from this directory with:
```text
python ../using_rust_extension.py
```
