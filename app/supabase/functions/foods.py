from app.supabase import supabase


def get_foods():
    res = supabase.from_("foods").select("""
            *,
            food_products_food_id(amount, product:product_id(name, id)
            """).execute()
    return res.data


def get_food_by_id(food_id: int):
    res = supabase.from_("foods").select("*").eq("id", food_id).execute()
    return res.data


def upsert_food(data):
    try:
        res = supabase.table("foods").upsert(data).execute()
        return res.data
    except Exception as ex:
        raise ex

