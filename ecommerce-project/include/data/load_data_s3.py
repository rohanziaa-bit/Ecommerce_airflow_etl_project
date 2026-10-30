def upload_to_s3():
   import boto3
   from pathlib import Path

   data_dir = Path(__file__).parent

   bucket_name = "ecommerce-snowflake-datawarehouse-project"

   s3 = boto3.client("s3")

   files = [
      "products_Clean.csv",
      "user_clean.csv",
      "carts_clean.csv"
    ]

   for file_name in files:
       file_path = data_dir / file_name


       s3.upload_file(
        str(file_path),
        bucket_name,
        f"cleaned/{file_name}"
    )

       print (f"Uploaded: {file_name}")