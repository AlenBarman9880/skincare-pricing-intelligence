import pandas as pd

df = pd.read_csv(
    "data/processed/nykaa_products_featured.csv"
)

df["suggested_price"] = df["effective_price"]

df.loc[
    df["reviews"] > 100000,
    "suggested_price"
] = (
    df["effective_price"] * 1.05
).round()
print(
    df[
        [
            "product_name",
            "effective_price",
            "suggested_price"
        ]
    ].head()
)

df.loc[
    df["reviews"] < 5000,
    "suggested_price"
] = (
    df["effective_price"] * 0.90
).round()

df.loc[
    df["price_tier"] == "Premium",
    "suggested_price"
] = (
    df["suggested_price"] * 1.03
).round()

df.loc[
    df["discount"] >= 20,
    "suggested_price"
] = df["effective_price"]

df["price_change"] = (
    df["suggested_price"]
    -
    df["effective_price"]
)

print(
    df[
        [
            "effective_price",
            "suggested_price",
            "price_change"
        ]
    ].head()
)

df["pricing_action"] = "Keep Price"

df.loc[
    df["price_change"] > 0,
    "pricing_action"
] = "Increase Price"


df.loc[
    df["price_change"] < 0,
    "pricing_action"
] = "Decrease Price"

print(
    df[
        [
            "product_name",
            "pricing_action"
        ]
    ].head()
)

print()

print("Pricing Summary")

print(
    df["pricing_action"].value_counts()
)

df.to_csv(
    "data/processed/nykaa_products_pricing.csv",
    index=False
)

print()

print("Pricing dataset saved successfully!")
print()

print(df.info())

print()

print(df.head())