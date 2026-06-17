import pandas as pd

df = pd.read_csv(
    "data/processed/nykaa_products_normalized.csv"
)

print(df.head(100))

df["promo_code"] = None

print(
    df[
        [
            "product_name",
            "promo_code"
        ]
    ].head()
)

df["loyalty_discount"] = 0

print(
    df[
        [
            "product_name",
            "loyalty_discount"
        ]
    ].head()
)

def fake_discount(row):

    if row["discount"] == 0:
        return False

    if row["original_price"] <= row["discounted_price"]:
        return True

    return False

df["fake_discount"] = df.apply(
    fake_discount,
    axis=1
)
print(

    df[
        [
            "original_price",
            "discounted_price",
            "discount",
            "fake_discount"
        ]
    ].head()

)
print(

    "Fake Discounts Found:",
    df["fake_discount"].sum()

)

print("\nData Quality Scorecard\n")

print(
    "Rows:",
    len(df)
)

print(
    "Columns:",
    len(df.columns)
)

print(
    "Missing Values:"
)

print(
    df.isnull().sum()
)

print(
    "\nDuplicate Rows:",
    df.duplicated().sum()
)

total_cells = df.shape[0] * df.shape[1]

missing_cells = df.isnull().sum().sum()

completeness = (
    (total_cells - missing_cells)
    /
    total_cells
) * 100

print(
    f"\nDataset Completeness: {completeness:.2f}%"
)

df.to_csv(
    "data/processed/final_quality_checked.csv",
    index=False
)

print("\nQuality checked dataset saved successfully!")

print("\nFinal Dataset Information\n")

print(df.info())

print("\nFinal Columns\n")

print(df.columns.tolist())

print("\nSample Data\n")

print(df.head())