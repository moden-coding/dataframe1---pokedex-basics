# Pokédex Basics

Use pandas to answer basic questions about a table of 800 Pokémon.

## What to write

Fill in the three functions in `src/pokedex.py`.

| Function | What it returns |
|---|---|
| `stat_summary(df, column)` | (row count, column mean rounded to 1 decimal, column max) |
| `strongest(df, column)` | the Name of the Pokémon with the highest value in column |
| `category_report(df, column)` | (most common value in column, number of distinct values) |

Every function must work for any column you pass in, not just the ones in the examples.

## Examples

Using the full Pokémon data:

```python
stat_summary(df, "Attack")      # (800, 79.0, 190)
strongest(df, "Sp. Atk")        # 'MewtwoMega Mewtwo Y'
strongest(df, "HP")             # 'Blissey'
category_report(df, "Type 2")   # ('Flying', 18)
category_report(df, "Type 1")   # ('Water', 18)
```

Run `python src/pokedex.py` to see the first three printed.

## Running the tests

In a terminal, from the assignment folder:

```
python -m unittest discover
```

Or open the Testing panel in VS Code (the flask icon) and run the "Python Tests" tree.

## If tests won't run

- **"No module named pandas"**: select the conda/Anaconda interpreter (Cmd/Ctrl+Shift+P → Python: Select Interpreter), then trash the terminal and open a new one.
- If you have the extension **"Python Test Explorer for Visual Studio Code"** installed, uninstall it. It ignores your interpreter choice.
- Open the assignment folder itself in VS Code (File → Open Folder), not a folder above it.
- **Windows**: if conda won't activate in the terminal, run `conda init powershell` once in Anaconda Prompt and restart VS Code.
