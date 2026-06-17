import pandas as pd
df = pd.read_csv(
    "data/raw/nykaa_products.csv"
)
print(df.head())

print(df.info())

print(df.isnull().sum())
df["original_price"] = (
    df["original_price"]
    .str.replace("₹", "", regex=False)
)

df["original_price"] = pd.to_numeric(
    df["original_price"],
    errors="coerce"
)
df["discounted_price"] = (
    df["discounted_price"]
    .str.replace("₹", "", regex=False)
)

df["discounted_price"] = pd.to_numeric(
    df["discounted_price"],
    errors="coerce"
)
print(df[["original_price", "discounted_price"]].head())

print(df.dtypes)
df["discount"] = (
    df["discount"]
    .str.replace("% Off", "", regex=False)
)

df["discount"] = pd.to_numeric(
    df["discount"],
    errors="coerce"
)
df["rating"] = (
    df["rating"]
    .str.extract(r"(\d+)")
)

df["rating"] = pd.to_numeric(
    df["rating"]
)
df["reviews"] = (
    df["reviews"]
    .str.replace(" reviews", "", regex=False)
)

df["reviews"] = pd.to_numeric(
    df["reviews"]
)
df["original_price"] = df["original_price"].fillna(
    df["discounted_price"]
)

df["discount"] = df["discount"].fillna(0)
print(
    "Rows before:",
    len(df)
)

print(
    "Duplicate Products:",
    df.duplicated(
        subset=["product_name"]
    ).sum()
)
df = df.drop_duplicates(
    subset=["product_name"]
)
print(
    "Rows after:",
    len(df)
)
df["scraped_at"] = pd.to_datetime(
    df["scraped_at"]
)
print("\nFinal Dataset Info\n")
df["original_price"] = df["original_price"].astype(int)

df["discount"] = df["discount"].astype(int)
print(df.info())

print(df.head())

print(df.isnull().sum())
import os

os.makedirs(
    "data/processed",
    exist_ok=True
)

df.to_csv(
    "data/processed/nykaa_products_clean.csv",
    index=False
)

print(
    "\nProcessed dataset saved successfully!"
)