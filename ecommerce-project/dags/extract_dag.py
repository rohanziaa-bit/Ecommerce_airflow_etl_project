from datetime import datetime,timedelta
from airflow.sdk import dag,task
from pathlib import Path

default_args = {
    "owner": "areeb",
    "retries": 2,
    "retry_delay": timedelta(minutes=2)

}

@dag(
    dag_id="ecommerce_api_pipeline",
    default_args=default_args,
    start_date = datetime(2026,1,1),
    schedule='*/2 * * * *',
    catchup=False,
    tags=["ecommerce","api","transform","s3"]
)

def ecommerce_full_pipeline():

    @task
    def extract_product_task():
        from include.extract_apis import extract_products 
        extract_products()
    @task
    def extract_cart_task():
        from include.extract_apis import extract_cart 
        extract_cart()

    @task
    def extract_users_Task():
        from include.extract_apis import extract_user 
        extract_user()
    
    @task
    def transform_products_task():
        from include.data.transformation import transform_products
        transform_products()
    
    @task
    def transform_users_task():
        from include.data.transformation import transform_user
        transform_user()
    @task
    def transform_carts_task():
        from include.data.transformation import transformed_Carts
        transformed_Carts()
        
    @task
    def upload_to_S3_task():
        from include.data.load_data_s3 import upload_to_s3
        upload_to_s3()


    products = extract_product_task()
    user =   extract_users_Task()
    carts = extract_cart_task()


    products_clean = transform_products_task()
    users_clean = transform_users_task()
    carts_Clean = transform_carts_task()

    s3_upload = upload_to_S3_task()


    products >> products_clean
    user >> users_clean
    carts >> carts_Clean

    [products_clean, users_clean,carts_Clean] >> s3_upload

ecommerce_full_pipeline()
