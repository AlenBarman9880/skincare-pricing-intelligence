import pandas as pd

df = pd.read_csv(
    "data/processed/nykaa_products_pricing.csv"
)

print(df.head())

df["recommendation"] = "Monitor"
print(df["recommendation"].head())

df.loc[
    df["reviews"] > 100000,
    "recommendation"
] = "Best Seller"

df.loc[
    (df["price_tier"] == "Premium") &
    (df["discount"] < 10),
    "recommendation"
] = "Increase Discount"

df.loc[
    (df["price_tier"] == "Budget") &
    (df["reviews"] > 50000),
    "recommendation"
] = "Increase Price Slightly"

df.loc[
    df["discount"] >= 20,
    "recommendation"
] = "Promotion Running"

df.loc[
    df["rating"] <= 3,
    "recommendation"
] = "Improve Product"

print()

print(
    df[
        [
            "product_name",
            "price_tier",
            "discount",
            "reviews",
            "recommendation"
        ]
    ].head(10)
)

print()

print("Recommendation Summary")

print(
    df["recommendation"].value_counts()
)

df.to_csv(
    "data/processed/nykaa_products_recommendations.csv",
    index=False
)

print()

print("Recommendation dataset saved successfully!")

print()

print(df.info())

print()

print(df.head())