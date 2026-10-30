{{ config(materialized = "table") }}

SELECT
    p.CART_ID,
    p.CUSTOMER_ID,
    u.FULL_NAME,
    u.CITY,
    p.PRODUCT_ID,
    p.PRODUCT_NAME,
    p.QUANTITY,
    p.PRICE,
    p.PRODUCT_TOTAL,
    p.PRODUCT_DISCOUNTED_TOTAL,
    ROUND(p.PRODUCT_TOTAL - p.PRODUCT_DISCOUNTED_TOTAL, 2) AS DISCOUNT_AMOUNT,
    p.BRAND,
    p.PRODUCT_RATING,
    p.STOCK_STATUS
FROM {{ ref('int_cart_product') }} AS p
INNER JOIN {{ ref('int_user_product') }} AS u
    ON p.CUSTOMER_ID = u.CUSTOMER_ID