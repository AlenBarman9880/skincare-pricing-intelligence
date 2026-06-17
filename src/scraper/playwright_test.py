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
    titles = soup.find_all(
        "h2",
        class_="css-xrzmfa"
    )

    print(
        "Titles Found:",
        len(titles)
    )

    print("\nFirst 5 Products:\n")

    for title in titles[:5]:
        print(title.get_text(strip=True))
        import os

    os.makedirs(
        "data/raw",
        exist_ok=True
    )
    with open(
        "data/raw/nykaa_page.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)

    print("HTML saved successfully")
    
    input("Press Enter to close browser...")

    browser.close()