# Python Experiments

Most of these were created in the process of creating my book that introduces the foundations of concurrency (still in development at this writing). Each subdirectory represents an experiment or a group of experiments.

Each project uses the [`rye` tool](https://rye-up.com/) for creation and maintenance, and I assume the reader will also be using `rye`. However, `rye` creates `pyproject.toml` files so these may work with other systems such as `poetry`.

To provision an experiment with tools, move into that directory (where you will see the `pyproject.toml` file) and run `rye sync`. This will create a virtual environment and fetch the necessary libraries into that venv. In addition, `rye` provides a local version of Python, so you do not need to install a global Python in order to run any of the experiments—you only need to install `rye`. When you move into an experiment's directory, or any of its subdirectories, that local version of Python and everything else in that virtual environment is automatically available (you do not have to explicitly start and shut down the virtual environment). Thus you can run Python programs in that experiment the way you always do:
`python script_file.py`.

Some experiments use development tools such as `mypy`. You must run these through `rye`, using `rye run`. For example:

```text
rye run mypy .
```
