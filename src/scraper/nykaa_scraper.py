from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "https://www.nykaa.com/search/result/?q=niacinamide%20serum&root=search&searchType=Manual&sourcepage=Search+Page",
        wait_until="domcontentloaded",
        timeout=60000
    )
    page.wait_for_timeout(5000)
    print(page.title())
    html = page.content()
    soup = BeautifulSoup(
        html,
        "html.parser"
    )
    product_cards = soup.find_all(
        "div",
        class_="productWrapper css-17nge1h"
    )
    print(
        "Cards Found:",
        len(product_cards)
    )
    products = []

    for card in product_cards:

        # Product Name
        title_tag = card.find(
            "h2",
            class_="css-xrzmfa"
        )

        title = (
            title_tag.get_text(strip=True)
            if title_tag
            else None
        )

        # Original Price
        original_price_tag = card.find(
            "span",
            class_="css-17x46n5"
        )

        original_price = (
            original_price_tag.get_text(strip=True)
            if original_price_tag
            else None
        )

        # Discounted Price
        discounted_price_tag = card.find(
            "span",
            class_="css-111z9ua"
        )

        discounted_price = (
            discounted_price_tag.get_text(strip=True)
            if discounted_price_tag
            else None
        )

        # Discount
        discount_tag = card.find(
            "span",
            class_="css-cjd9an"
        )

        discount = (
            discount_tag.get_text(strip=True)
            if discount_tag
            else None
        )

        # Rating
        rating_tag = card.find(
            "div",
            class_="css-wskh5y"
        )

        rating = (
            rating_tag.get("aria-label")
            if rating_tag
            else None
        )

        # Reviews
        reviews_tag = card.find(
            "span",
            class_="css-1qbvrhp"
        )

        reviews = (
            reviews_tag.get("aria-label")
            if reviews_tag
            else None
        )

        products.append({
            "product_name": title,
            "original_price": original_price,
            "discounted_price": discounted_price,
            "discount": discount,
            "rating": rating,
            "reviews": reviews
        })

import pandas as pd
from datetime import datetime

df = pd.DataFrame(products)

df["scraped_at"] = datetime.now()

print(df.head())

print(
    f"\nTotal Products Scraped: {len(df)}"
)

import os

os.makedirs(
    "data/raw",
    exist_ok=True
)

df.to_csv(
    "data/raw/nykaa_products.csv",
    index=False
)

print(
    "\nCSV saved successfully!"
)
print(df.info())