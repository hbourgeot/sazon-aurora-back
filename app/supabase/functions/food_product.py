from app.supabase import supabase


def get_food_productss():
    res = supabase.table("food_products").select("*").execute()
    print(res)


def get_food_products_by_id(food_id: int, product_id: int):
    res = supabase.table("food_products").select("*").eq("food_id", food_id).eq("product_id", product_id).execute()
    return res.data


def upsert_food_product(data):
    # Assuming get_food_products_by_id is implemented correctly
    fp = get_food_products_by_id(data["food_id"], data["product_id"])

    if fp:
        # Update the existing record
        res = supabase.table("food_products").update({"amount": data["amount"]}).eq(
            "food_id", data["food_id"]).eq("product_id", data["product_id"]).execute()
    else:
        # Insert a new record
        res = supabase.table("food_products").insert(data).execute()

    return res.data
