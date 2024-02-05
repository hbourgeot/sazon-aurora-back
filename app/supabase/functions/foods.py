from app.supabase import supabase


def get_foods():
    res = supabase.table("foods").select("""*, products:food_products (amount, product:product_id (id, name))""").execute()
    return res.data

def get_food_by_id(food_id: int):
    res = supabase.table("foods").select("*, products:food_products (amount, product:product_id (id, name))").eq("id", food_id).execute()
    return res.data


def upsert_food(data):
    try:
        res = supabase.table("foods").upsert(data).execute()
        return res.data
    except Exception as ex:
        raise ex

