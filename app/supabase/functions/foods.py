from app.supabase import supabase
from fastapi import UploadFile

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

def upload_file(file: UploadFile, food: str, number: int):
    try:
        res = supabase.storage.from_("images").upload(file.file, path=f"foods/{food}-{number}.{file.filename.split('.')[-1]}" )
        return res.data
    except Exception as ex:
        raise ex
    
def get_images_from_food(food: str, number: int):
    try:
        res = supabase.storage.from_("images").get_public_url(f"foods/{food}-{number}.*")
        return res.data
    except Exception as ex:
        raise ex