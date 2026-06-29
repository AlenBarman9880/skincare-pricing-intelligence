import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/nykaa_products_featured.csv")
recommendations = pd.read_csv(
    "data/processed/nykaa_products_recommendations.csv"
)

st.set_page_config(
    page_title="Skincare Pricing Command Center",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Skincare Pricing Intelligence")
st.caption(
    "Competitive Pricing Intelligence Platform | Executive Dashboard"
)

st.markdown("---")
st.subheader("Executive Command Center")

# Sidebar Filters
st.sidebar.header("Filters")

brand = st.sidebar.selectbox(
    "Brand",
    ["All"] + sorted(df["brand"].unique().tolist())
)

price_tier = st.sidebar.selectbox(
    "Price Tier",
    ["All"] + sorted(df["price_tier"].unique().tolist())
)

recommendation = st.sidebar.selectbox(
    "Recommendation",
    ["All"] + sorted(
        recommendations["recommendation"].unique().tolist()
    )
)

search = st.sidebar.text_input("Search Product")

# Apply Filters
filtered_df = df.copy()

if brand != "All":
    filtered_df = filtered_df[
        filtered_df["brand"] == brand
    ]

if price_tier != "All":
    filtered_df = filtered_df[
        filtered_df["price_tier"] == price_tier
    ]

if search:
    filtered_df = filtered_df[
        filtered_df["product_name"]
        .str.contains(search, case=False)
    ]

filtered_rec = recommendations.copy()

if recommendation != "All":
    filtered_rec = filtered_rec[
        filtered_rec["recommendation"] == recommendation
    ]

#KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Products",
    len(filtered_df)
)

col2.metric(
    "Average Price",
    f"₹{filtered_df['effective_price'].mean():.0f}"
)

col3.metric(
    "Average Rating",
    round(filtered_df["rating"].mean(), 2)
)

col4.metric(
    "Average Discount",
    f"{filtered_df['discount'].mean():.1f}%"
)

st.markdown("---")
st.subheader("📈 Competitor Price Tracker")

price_df = filtered_df.sort_values("effective_price")

st.line_chart(
    price_df.set_index("product_name")["effective_price"]
)

st.markdown("---")
st.subheader("🏷 Brand-wise Average Price")

brand_price = (
    filtered_df
    .groupby("brand")["effective_price"]
    .mean()
    .sort_values()
)

st.bar_chart(brand_price)

st.markdown("---")
st.subheader("💰 Price Tier Distribution")

fig, ax = plt.subplots(figsize=(6,6))

filtered_df["price_tier"].value_counts().plot.pie(
    autopct="%1.1f%%",
    ax=ax
)

ax.set_ylabel("")

st.pyplot(fig)


st.markdown("---")
st.subheader("⭐ Top 10 Popular Products")

top_products = (
    filtered_df
    .sort_values(
        "popularity_score",
        ascending=False
    )
    [["product_name","popularity_score"]]
    .head(10)
)

st.dataframe(
    top_products,
    use_container_width=True
)

st.markdown("---")
st.subheader("🔥 Highest Discount Products")

discount_products = (
    filtered_df
    .sort_values(
        "discount",
        ascending=False
    )
    [["product_name","discount","effective_price"]]
    .head(10)
)

st.dataframe(
    discount_products,
    use_container_width=True
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏷 Brand-wise Average Price")
    st.bar_chart(brand_price)


col3, col4 = st.columns(2)

with col3:
    st.subheader("💰 Price Tier Distribution")
    st.pyplot(fig)

with col4:
    st.subheader("📈 Competitor Price Tracker")
    st.line_chart(
        price_df.set_index("product_name")["effective_price"]
    )

st.subheader("Executive Summary")

avg_price = filtered_df["effective_price"].mean()
avg_discount = filtered_df["discount"].mean()

highest_rated = (
    filtered_df
    .sort_values("rating", ascending=False)
    .iloc[0]["product_name"]
)

st.info(f"""
• Products Tracked : {len(filtered_df)}

• Average Effective Price : ₹{avg_price:.0f}

• Average Discount : {avg_discount:.1f}%

• Highest Rated Product :
{highest_rated}
""")

best_discount = filtered_df.loc[
    filtered_df["discount"].idxmax()
]

st.success(
    f"🔥 Highest Discount: "
    f"{best_discount['product_name']} "
    f"({best_discount['discount']}%)"
)

#Data Preview
st.markdown("---")

st.subheader("Filtered Products")

st.dataframe(
    filtered_df,
    use_container_width=True
)


## Dashboard

st.header("Pricing Recommendation Center")
st.subheader("Recommendation Summary")

st.write(
    recommendations["recommendation"]
    .value_counts()
)

recommendation_counts = (
    filtered_rec["recommendation"]
    .value_counts()
)

st.bar_chart(recommendation_counts)


st.dataframe(
    filtered_rec[
        [
            "product_name",
            "brand",
            "discounted_price",
            "pricing_action",
            "recommendation"
        ]
    ]
)

st.subheader("Recommendation Highlights")
increase = len(
    filtered_rec[
        filtered_rec["recommendation"] == "Increase Price"
    ]
)
decrease = len(
    filtered_rec[
        filtered_rec["recommendation"] == "Decrease Price"
    ]
)
maintain = len(
    filtered_rec[
        filtered_rec["recommendation"] == "Maintain Price"
    ]
)

st.write(f"⬆ Increase Price : {increase}")
st.write(f"⬇ Decrease Price : {decrease}")
st.write(f"➡ Maintain Price : {maintain}")

st.success(
    "Pricing recommendations generated successfully."
)

st.header("Recommendation KPIs")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Recommendations",
    len(filtered_rec)
)

col2.metric(
    "Increase Price",
    len(
        filtered_rec[
            filtered_rec["recommendation"] == "Increase Price"
        ]
    )
)

col3.metric(
    "Decrease Price",
    len(
        filtered_rec[
            filtered_rec["recommendation"] == "Decrease Price"
        ]
    )
)

csv = filtered_rec.to_csv(index=False)

st.download_button(
    label="📥 Download Recommendations",
    data=csv,
    file_name="pricing_recommendations.csv",
    mime="text/csv"
)

st.markdown("---")

st.caption(
    """
Skincare Pricing Intelligence Platform

Developed using

• Python

• Playwright

• Pandas

• PostgreSQL

• Streamlit

• Matplotlib
"""
)