from app.supabase import supabase


def get_foods():
    res = supabase.from_("foods").select("*").execute()
    print(res)
    return res


def get_food_by_id(food_id: int):
    res = supabase.from_("foods").select("*").eq("id", food_id)
    print(res)
    return res


def upsert_food(data):
    try:
        res = supabase.table("foods").upsert(data).execute()
        print(res)
        return res
    except Exception as ex:
        raise ex

