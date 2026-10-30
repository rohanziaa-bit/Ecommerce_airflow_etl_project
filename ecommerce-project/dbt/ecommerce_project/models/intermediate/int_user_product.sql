{{ config(materialized = "view")}}

SELECT 
 C.CUSTOMER_ID,
 C.FIRST_NAME || '' || C.LAST_NAME AS FULL_NAME,
 C.EMAIL,
 C.PHONE,
 C.GENDER,
 C.CITY,
 I.CART_ID,
 I.PRODUCT_TOTAL,
 I.PRODUCT_DISCOUNTED_TOTAL
 FROM {{ ref('stg_cart')}} as I
 inner join {{ ref('stg_user')}} as C
   on I.CUSTOMER_ID = C.CUSTOMER_ID
