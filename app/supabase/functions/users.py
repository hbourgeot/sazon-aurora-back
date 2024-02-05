from app.supabase import supabase


def get_user():
    res = supabase.table("users").select("*").execute()
    print(res)
    return res


def get_user_by_id(user_id: int):
    res = supabase.table("users").select("*").eq("id", user_id).execute()
    print(res)
    return res

def upsert_user(data):
    res = supabase.table("users").upsert(data).execute()
    print(res)
    return res

