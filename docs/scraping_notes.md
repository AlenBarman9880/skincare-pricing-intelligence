# Nykaa Scraping Notes

## Serum Category

### Sample Product

Product Name:Minimalist 10% Niacinamide Face Serum With Matmarine + Zinc
HTML tag:<h2 class="css-xrzmfa">Minimalist 10% Niacinamide Face Serum With Matmarine + Zinc ...</h2>

Price:₹249
Discounted Price:₹237
HTML tag:<span class="css-1yjfidh">Regular price ₹249. Discounted price ₹237. 5% Off.</span>

Discount:5% Off
HTML tag:<span class="css-1yjfidh">Regular price ₹249. Discounted price ₹237. 5% Off.</span>

Rating:4 out of 5 star rating
HTML tag:<div class="css-wskh5y" aria-label="4 out of 5 star rating">
Reviews:128784 reviews
HTML tag:<span aria-label="128784 reviews" class="css-1qbvrhp">(128784)</span>

Category URL: https://www.nykaa.com/search/result/?q=niacinamide%20serum&root=search&searchType=Manual&sourcepage=Search+Page

## Face Wash Category

### Sample Product

Product Name:Dot &amp; Key Vitamin C + E Super Bright Gel Face Wash
HTML tag:<h2 class="css-xrzmfa">Dot &amp; Key Vitamin C + E Super Bright Gel Face Wash</h2>

Price:₹249
Discounted Price:₹214
HTML tag:<span class="css-1yjfidh">Regular price ₹249. Discounted price ₹214. 14% Off.</span>

Discount:14% Off
HTML tag:<span class="css-1yjfidh">Regular price ₹249. Discounted price ₹214. 14% Off.</span>

Rating:4 out of 5 star rating
HTML tag:<div aria-label="4 out of 5 star rating" class="css-wskh5y">
Reviews:37638 reviews
HTML tag:<span aria-label="37638 reviews" class="css-1qbvrhp">(37638)</span>

Category URL: https://www.nykaa.com/skin/cleansers/face-wash/c/8379?search_redirection=True

## Mosturiser Category

### Sample Product

Product Name:Plum 2% Niacinamide &amp; Rice Water Moisturiser - Lightweight G...
HTML tag:<h2 class="css-xrzmfa">Plum 2% Niacinamide &amp; Rice Water Moisturiser - Lightweight G...</h2>

Price:₹525
Discounted Price:₹473
HTML tag:<span class="css-1yjfidh">Regular price ₹525. Discounted price ₹473. 10% Off.</span>

Discount:10% Off
HTML tag:<span class="css-1yjfidh">Regular price ₹525. Discounted price ₹473. 10% Off.</span>

Rating:4 out of 5 star rating
HTML tag:<div class="css-wskh5y" aria-label="4 out of 5 star rating">
Reviews:27590 reviews
HTML tag:<span aria-label="27590 reviews" class="css-1qbvrhp">(27590)</span>

Category URL: https://www.nykaa.com/skin/moisturizers/c/8393?search_redirection=True

## Selector Stability Assessment

### Product Name

Selector: h2.css-xrzmfa

Observed In:
- Serum
- Face Wash
- Moisturizer

Stability: Medium

Reason:
The selector remained consistent across all three categories. However, the class name appears auto-generated (css-xrzmfa) rather than semantic (e.g., product-title), which means it may change after website updates.

Alternative Strategy:
Locate the product title relative to the product card container instead of relying solely on the CSS class.

### Price / Discount

Selector: span.css-1yjfidh

Observed In:
- Serum
- Face Wash
- Moisturizer

Stability: Medium

Reason:
The same selector contains regular price, discounted price, and discount information across categories. The structure appears reusable, but the class name is still auto-generated.

Alternative Strategy:
Extract price information using text patterns (₹ symbol, "Discounted price", "% Off") in addition to the CSS selector.

### Rating

Selector: div.css-wskh5y

Observed In:
- Serum
- Face Wash
- Moisturizer

Stability: Medium-High

Reason:
The rating information is stored inside the aria-label attribute ("4 out of 5 star rating"), which is generally more stable than CSS classes.

Alternative Strategy:
Use aria-label extraction instead of depending only on the class name.

### Review Count

Selector: span.css-1qbvrhp

Observed In:
- Serum
- Face Wash
- Moisturizer

Stability: Medium-High

Reason:
Review counts are exposed through the aria-label attribute ("128784 reviews"), which tends to be maintained for accessibility purposes.

Alternative Strategy:
Prioritize aria-label extraction over class-based extraction.