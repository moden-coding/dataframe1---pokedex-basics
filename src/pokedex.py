import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/modengann/Data-sets/refs/heads/master/pokemon.csv"


def stat_summary(df: pd.DataFrame, column: str) -> tuple:
    """Return (row count, column mean rounded to 1 decimal, column max)."""
    pass


def strongest(df: pd.DataFrame, column: str) -> str:
    """Return the Name of the Pokémon with the highest value in column."""
    pass


def category_report(df: pd.DataFrame, column: str) -> tuple:
    """Return (most common value in column, number of distinct values)."""
    pass


def main():
    df = pd.read_csv(DATA_URL)
    print(stat_summary(df, "Attack"))
    print(strongest(df, "Sp. Atk"))
    print(category_report(df, "Type 2"))


if __name__ == "__main__":
    main()
