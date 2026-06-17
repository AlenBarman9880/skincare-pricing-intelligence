import pandas as pd
import re
df = pd.read_csv(
    "data/processed/nykaa_products_clean.csv"
)

print(df.head(25))

df["currency"] = "INR"
exchange_rates = {
    "INR":1,
    "USD":86,
    "EUR":98
}

def convert_to_inr(price, currency):

    return price * exchange_rates[currency]
df["price_inr"] = df.apply(
    lambda row:
        convert_to_inr(
            row["discounted_price"],
            row["currency"]
        ),
    axis=1
)

FREE_SHIPPING_THRESHOLD = 499
DEFAULT_SHIPPING_COST = 40
df["shipping_cost"] = DEFAULT_SHIPPING_COST
df.loc[
    df["discounted_price"] >= FREE_SHIPPING_THRESHOLD,
    "shipping_cost"
] = 0

df["effective_price"] = (
    df["discounted_price"]
    +
    df["shipping_cost"]
)

def extract_size(product):

    match = re.search(
        r'(\d+)\s?(ml|g)',
        product,
        re.IGNORECASE
    )

    if match:

        return int(
            match.group(1)
        )

    return None

df["size"] = df[
    "product_name"
].apply(
    extract_size
)

df["price_per_unit"] = (
    df["effective_price"]
    /
    df["size"]
)
df["price_per_unit"] = df["price_per_unit"].fillna(0)
df["price_per_unit"] = df["price_per_unit"].astype(float)
print(
    df[
        [
            "effective_price",
            "size",
            "price_per_unit"
        ]
    ].head()
)
# Size information is unavailable from Nykaa search results.
# price_per_unit is set to 0 until product-detail-page scraping is implemented.

df.to_csv(
    "data/processed/nykaa_products_normalized.csv",
    index=False
)

print(
    "Normalized dataset saved successfully!"
)

print("\nFinal Dataset Info\n")

print(df.info())

print("\nColumns:\n")

print(df.columns.tolist())