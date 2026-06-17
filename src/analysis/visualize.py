import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/nykaa_products_featured.csv"
)

brand_count = (
    df["brand"]
    .value_counts()
)

plt.figure(figsize=(8,5))

brand_count.plot(
    kind="bar"
)

plt.title("Products by Brand")
plt.xlabel("Brand")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig(
    "reports/charts/brand_count.png",
    dpi=300
)

plt.close()


plt.figure(figsize=(8,5))

plt.hist(
    df["discounted_price"],
    bins=8
)

plt.title("Price Distribution")
plt.xlabel("Price (INR)")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    "reports/charts/price_distribution.png",
    dpi=300
)

plt.close()


brand_price = (
    df.groupby("brand")["discounted_price"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(9,5))

brand_price.plot(
    kind="bar"
)

plt.title("Average Price by Brand")
plt.xlabel("Brand")
plt.ylabel("Average Price")

plt.tight_layout()

plt.savefig(
    "reports/charts/average_brand_price.png",
    dpi=300
)

plt.close()


bucket = (
    df["discount_bucket"]
    .value_counts()
)

plt.figure(figsize=(6,4))

bucket.plot(
    kind="bar"
)

plt.title("Discount Categories")
plt.xlabel("Bucket")
plt.ylabel("Products")

plt.tight_layout()

plt.savefig(
    "reports/charts/discount_bucket.png",
    dpi=300
)

plt.close()


tier = (
    df["price_tier"]
    .value_counts()
)

plt.figure(figsize=(6,4))

tier.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Price Tier Distribution")

plt.tight_layout()

plt.savefig(
    "reports/charts/price_tier.png",
    dpi=300
)

plt.close()


print("Charts saved successfully!")