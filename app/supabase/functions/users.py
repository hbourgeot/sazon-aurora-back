from app.supabase import supabase
from app.supabase.functions.cart import get_foods_recommendations as cart_get_foods_recommendations
from app.supabase.functions.invoice import get_foods_recommendations as invoice_get_foods_recommendations

def get_user():
    res = supabase.table("users").select("*").execute()
    return res


def get_cart_and_invoice(user_id: int):
    cfr = cart_get_foods_recommendations(user_id)
    ifr = invoice_get_foods_recommendations(user_id)

    # Combina las listas y elimina duplicados
    combined_list = []
    for item in cfr + ifr:
        if item not in combined_list:
            combined_list.append(item)

    # Convierte cada objeto de la lista combinada en un string
    combined_list_as_strings = []
    for item in combined_list:
        # Asumiendo que cada item es un diccionario, formatea la información deseada en un string
        # Ajusta las claves ('name', 'description', 'price') según tu estructura de datos
        item_string = f"Name: {item.get('name', '')}, Description: {item.get('description', '')}, Price: {item.get('price', '')}"
        combined_list_as_strings.append(item_string)

    return combined_list_as_strings
    

def get_user_by_id(user_id: int):
    res = supabase.table("users").select("*").eq("id", user_id).execute()
    return res

def upsert_user(data):
    res = supabase.table("users").upsert(data).execute()
    return res

