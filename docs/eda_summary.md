Phase 4 — Basic statistics
       original_price  discounted_price  ...  price_segment_id  popularity_score
count       20.000000          20.00000  ...         20.000000         20.000000
mean       813.500000         739.40000  ...          1.900000     120924.650000
std        532.129535         523.95273  ...          0.718185     203803.511087
min        249.000000         237.00000  ...          1.000000         15.000000
25%        574.000000         485.00000  ...          1.000000      11264.000000
50%        647.000000         556.00000  ...          2.000000      25652.000000
75%        992.250000         863.00000  ...          2.000000      65614.000000
max       2000.000000        2000.00000  ...          3.000000     652472.000000

Phase 5 — Brand frequency
Plum                3
Minimalist          2
The Derma Co        2
Cetaphil            2
The Ordinary        1
Deconstruct         1
Hyphen              1
Foxtale             1
Dot & Key           1
SKIN1004            1
Pilgrim             1
Anua                1
Beauty Of Joseon    1
Underated           1
Lumineve            1
Name: count, dtype: int64

Phase 6 — Price tier frequency
Mid        10
Budget      6
Premium     4
Name: count, dtype: int64

Phase 7 — Discount bucket frequency
Medium    8
Low       7
High      5
Name: count, dtype: int64

Phase 8 — Average price
751.4

Phase 9 — Highest priced product
product_name        Anua Niacinamide 10 Txa 4 Serum, Brightening K...
original_price                                                   2000
discounted_price                                                 2000
discount                                                            0
rating                                                              4
reviews                                                          2021
scraped_at                                 2026-06-17 20:40:35.431121
currency                                                          INR
price_inr                                                        2000
shipping_cost                                                       0
effective_price                                                  2000
size                                                              NaN
price_per_unit                                                    0.0
category                                                        Serum
brand                                                            Anua
price_tier                                                    Premium
discount_bucket                                                   Low
price_segment_id                                                    3
popularity_score                                                 8084
Name: 15, dtype: object

Phase 10 — Lowest priced product
product_name        Minimalist 10% Niacinamide Face Serum With Mat...
original_price                                                    249
discounted_price                                                  237
discount                                                            5
rating                                                              4
reviews                                                        128784
scraped_at                                 2026-06-17 20:40:35.431121
currency                                                          INR
price_inr                                                         237
shipping_cost                                                      40
effective_price                                                   277
size                                                              NaN
price_per_unit                                                    0.0
category                                                        Serum
brand                                                      Minimalist
price_tier                                                     Budget
discount_bucket                                                   Low
price_segment_id                                                    1
popularity_score                                               515136
Name: 2, dtype: object
