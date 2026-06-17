import pandas as pd

from db_connection import get_connection
df = pd.read_csv(
    "data/processed/nykaa_products_clean.csv"
)
print(df.shape)

conn = get_connection()

cursor = conn.cursor()
for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO skincare_products
        (
            product_name,
            original_price,
            discounted_price,
            discount,
            rating,
            reviews,
            scraped_at
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            row["product_name"],
            row["original_price"],
            row["discounted_price"],
            row["discount"],
            row["rating"],
            row["reviews"],
            row["scraped_at"]
        )
    )

conn.commit()

cursor.close()

conn.close()

print("Data inserted successfully!")
