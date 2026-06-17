import pandas as pd
df = pd.read_csv(
    "data/processed/nykaa_products_normalized.csv"
)
print(df.head(100))

df["category"] = "Serum"
print(
    df[
        ["product_name","category"]
    ].head()
)

def extract_brand(product):

    known_brands = [
        "The Derma Co",
        "Dot & Key",
        "Beauty Of Joseon",
        "The Ordinary",
        "Minimalist",
        "Plum",
        "Pilgrim",
        "Foxtale",
        "Cetaphil",
        "Anua",
        "Hyphen",
        "Lumineve",
        "SKIN1004",
        "Deconstruct",
        "Underated"
    ]

    for brand in known_brands:

        if product.startswith(brand):

            return brand

    return product.split()[0]
df["brand"] = df["product_name"].apply(extract_brand)
print(
    df[
        ["product_name","brand"]
    ].head(10)
)
brand_counts = (
    df["brand"]
    .value_counts()
)
print(brand_counts)
def price_tier(price):

    if price < 500:
        return "Budget"

    elif price < 1000:
        return "Mid"

    else:
        return "Premium"
df["price_tier"] = df["discounted_price"].apply(price_tier)
print(
    df[
        [
            "effective_price",
            "price_tier"
        ]
    ].head(10)
)

def discount_bucket(discount):

    if discount <= 5:
        return "Low"

    elif discount <= 15:
        return "Medium"

    else:
        return "High"
df["discount_bucket"] = df["discount"].apply(discount_bucket)
print(
    df[
        [
            "discount",
            "discount_bucket"
        ]
    ].head(10)
)

price_map = {

    "Budget":1,
    "Mid":2,
    "Premium":3

}

df["price_segment_id"] = (
    df["price_tier"]
    .map(price_map)
)
print(
    df[
        [
            "price_tier",
            "price_segment_id"
        ]
    ].head()
)

df["popularity_score"] = (
    df["rating"]
    *
    df["reviews"]
)
print(
    df[
        [
            "brand",
            "rating",
            "reviews",
            "popularity_score"
        ]
    ].head()
)

df = (
    df.sort_values(
        by="popularity_score",
        ascending=False
    )
)
print(
    df[
        [
            "product_name",
            "popularity_score"
        ]
    ].head(10)
)

print(df.info())
print(df.head())
print(df.columns.tolist())

df.to_csv(
    "data/processed/nykaa_products_featured.csv",
    index=False
)

print(
    "Updated featured dataset saved successfully!"
)

