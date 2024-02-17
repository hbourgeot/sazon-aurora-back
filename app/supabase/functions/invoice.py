from app.supabase import supabase
from collections import Counter
from dateutil import parser

def get_foods_recommendations(user_id: int):
    res = supabase.table("invoices").select("*").eq("user_id", user_id).execute()

    if not res.data:
        return []
    
    foods = []
    for data in res.data:
        invoice_details = supabase.table("invoice_details").select(
            "*").eq("invoice_id", data["id"]).execute()


        food_ids = [x["food_id"] for x in invoice_details.data]
        for food_id in food_ids:
            food = supabase.table("foods").select("*").eq("id", food_id).limit(1).single().execute()

            appended_food = {
                "name": food.data["name"], "price": food.data["price"], "description": food.data["description"]}
            foods.append(appended_food)
    
    return foods


def get_sales():
    # Obtienes los datos de Supabase
    res = supabase.table("invoices").select("created_at").execute()

    # Verificas si la respuesta fue exitosa y tiene datos
    if res.data:
        # Conviertes las fechas a objetos date de Python
        fechas = [parser.parse(
            registro['created_at']).date() for registro in res.data]

        # Cuentas las ocurrencias de cada fecha
        conteo_por_fecha = Counter(fechas)

        # Si necesitas el resultado en un formato específico, puedes convertirlo aquí
        # Por ejemplo, convertirlo en una lista de diccionarios
        resultado = [{'fecha': fecha, 'ventas': conteo}
                     for fecha, conteo in conteo_por_fecha.items()]
        return resultado
    else:
        # Manejo de errores o datos vacíos
        return {"error": "No se pudieron obtener los datos"}

def get_invoices_join_by_id(invoice_id: int):
    res = supabase.table("invoices").select("created_at, total, user:user_id(id, name), details:invoice_details(id, quantity, price, food:food_id(id, name, description))").eq(
        "id", invoice_id).limit(1).single().execute()
    
    return res.data