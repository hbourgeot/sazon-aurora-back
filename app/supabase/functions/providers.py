from app.supabase import supabase


def get_providers():
    res = supabase.from_("providers").select("*").execute()
    return res


def get_provider_by_id(provider_id: int):
    res = supabase.from_("providers").select("*").eq("id", provider_id).execute()
    return res.data


def upsert_provider(data):
    res = supabase.table("providers").upsert(data).execute()
    return res.data

