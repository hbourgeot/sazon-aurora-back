from app.supabase import supabase


def get_roles():
    res = supabase.table("roles").select("*").execute()
    return res


def get_role_by_id(role_id: int):
    res = supabase.table("roles").select("*").eq("id", role_id).execute()
    return res


def upsert_role(data):
    try:
        res = supabase.table("roles").upsert(data).execute()
        return res
    except Exception as ex:
        raise ex

