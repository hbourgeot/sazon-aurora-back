from app.supabase import supabase

def get_products():
    res = supabase.table("products").select("*").execute()
    return res.data


def get_product_by_id(product_id: int):
    res = supabase.table("products").select("*").eq("id", product_id).execute()
    return res.data


def upsert_product(data):
    res = supabase.table("products").upsert(data).execute()
    return res.data

