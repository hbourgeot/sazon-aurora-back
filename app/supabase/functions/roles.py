from app.supabase import supabase


def get_roles():
    res = supabase.from_("roles").select("*").execute()
    print(res)
    return res


def get_role_by_id(role_id: int):
    res = supabase.from_("roles").select("*").eq("id", role_id).execute()
    print(res)
    return res


def upsert_role(data):
    try:
        res = supabase.table("roles").upsert(data).execute()
        print(res)
        return res
    except Exception as ex:
        raise ex

