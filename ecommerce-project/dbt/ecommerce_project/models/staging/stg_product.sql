{{ config(materialized = 'view')}}

SELECT
   ID as product_id,
   TRIM(TITLE) AS PRODUCT_NAME,
   LOWER(TRIM(CATEGORY)) AS category,
   PRICE AS price,
   RATING AS rating,
   STOCK AS stock,
   COALESCE(NULLIF(TRIM(BRAND), ''), 'NOT PROVIDED') AS brand

FROM {{ source('ecommerce','products')}}

where ID is not null  
   AND TITLE IS NOT NULL
   AND PRICE >= 0