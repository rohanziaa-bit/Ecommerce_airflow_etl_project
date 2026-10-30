
import json
from pathlib import Path

import requests

DATA_DIR = Path("/usr/local/airflow/include/data")
DATA_DIR.mkdir(parents=True, exist_ok=True)


def extract(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()


def extract_products():
    data = extract("https://dummyjson.com/products")

    with open(DATA_DIR / "products.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Products saved: {DATA_DIR / 'products.json'}")


def extract_cart():
    data = extract("https://dummyjson.com/carts")

    with open(DATA_DIR / "carts.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Carts saved: {DATA_DIR / 'carts.json'}")


def extract_user():
    data = extract("https://dummyjson.com/users")

    with open(DATA_DIR / "users.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Users saved: {DATA_DIR / 'users.json'}")
