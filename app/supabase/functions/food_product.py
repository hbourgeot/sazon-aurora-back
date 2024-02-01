from app.supabase import supabase


def get_food_productss():
    res = supabase.from_("food_products").select("*").execute()
    print(res)


def get_food_products_by_id(food_id: int):
    res = supabase.from_("food_products").select("*").eq("food_id", food_id)
    print(res)


def upsert_food_product(data):
    res = supabase.table("food_products").upsert(data).execute()
    print(res)
    return res.data

