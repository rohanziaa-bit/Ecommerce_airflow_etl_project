{{ config(materialized = "view") }}

SELECT
    CAST("c1" AS INTEGER) AS CUSTOMER_ID, -- ya fir CUSTOMER_ID likh kar check karein
    TRIM(INITCAP("c2")) AS FIRST_NAME,
    TRIM(INITCAP("c3")) AS LAST_NAME,
    NULLIF(LOWER(TRIM("c7")), '') AS EMAIL,
    TRIM("c8") AS PHONE,
    CASE
       WHEN UPPER(TRIM("c6")) = 'MALE' THEN 'Male'
       WHEN UPPER(TRIM("c6")) = 'FEMALE' THEN 'Female'
       WHEN UPPER(TRIM("c6")) = 'OTHER' THEN 'Other'
       ELSE NULL
    END AS GENDER,
    TRIM("c27") AS CITY

FROM {{ source('ecommerce', 'USERS_RAW') }}

WHERE "c1" IS NOT NULL
        