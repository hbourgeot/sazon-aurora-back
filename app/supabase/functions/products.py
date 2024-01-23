from app.supabase import supabase


def get_foods():
    res = supabase.from_("products").select("*").execute()
    return res.data


def get_food_by_id(food_id: int):
    res = supabase.from_("foods").select("*").eq("id", food_id).execute()
    return res.data


def upsert_food(data):
    res = supabase.table("foods").upsert(data).execute()
    return res.data

