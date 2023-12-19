from app.supabase import supabase


def get_foods():
    res = supabase.from_("foods").select("*").execute()
    print(res)


def get_food_by_id(food_id: int):
    res = supabase.from_("foods").select("*").eq("id", food_id)
    print(res)


def upsert_food(data):
    res = supabase.table("foods").upsert(data)
    print(res)

