import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent

def transform_products():
    df = pd.read_json(DATA_DIR / "products.json")


    if "products" in df.columns:
        df = pd.json_normalize(df["products"])


    df = df.drop(columns=["thumbnail"],errors="ignore")
    df = df.drop_duplicates(subset=["id"])

    df.to_csv(DATA_DIR / "products_Clean.csv",index=False)
    print ("Product transformed:",df.shape)


def transform_user():
    df = pd.read_json(DATA_DIR / "users.json")

    if "users" in df.columns:
        df = pd.json_normalize(df['users'])
    else:
        df = pd.json_normalize(df.to_dict(orient="records"))


    if "firstName" in df.columns and "lastName" in df.columns:
        df["Fullname"] = (
            df['firstName'].fillna("").astype(str)
            + " "
            + df["lastName"].fillna("").astype(str)

        ).str.strip()


    df = df.drop_duplicates()

    df.to_csv(DATA_DIR / "user_clean.csv", index=False)
    print ("User transformed",df.shape)


def transformed_Carts():
    df = pd.read_json(DATA_DIR / "carts.json")


    if "carts" in df.columns:
        df = pd.json_normalize(df["carts"])
    else:
        df = pd.json_normalize(df.to_dict(orient= "records"))

    if "products" in df.columns:
        df = df.explode("products",ignore_index=True)

        product_detail = pd.json_normalize(df["products"])
        product_detail.columns = [
            f"product_{col}" for col in product_detail.columns
        ]

        df = pd.concat(
            [df.drop(columns=["products"]), product_detail],
            axis=1
        )


    df = df.drop_duplicates()

    df.to_csv(DATA_DIR / "carts_clean.csv",index=False)
    print ("Carts transformed:",df.shape)


if __name__ == "__main__":
    transform_products()
    transform_user()
    transformed_Carts()