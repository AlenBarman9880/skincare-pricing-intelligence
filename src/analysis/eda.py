import pandas as pd

df = pd.read_csv(
    "data/processed/nykaa_products_featured.csv"
)

print(df.head())

print(df.describe())

print(df["brand"].value_counts())

print(df["price_tier"].value_counts())

print(df["discount_bucket"].value_counts())

print(
    df["effective_price"].mean()
)

print(
    df.loc[
        df["effective_price"].idxmax()
    ]
)

print(
    df.loc[
        df["effective_price"].idxmin()
    ]
)

