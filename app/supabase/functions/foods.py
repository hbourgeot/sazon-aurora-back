from app.supabase import supabase
from fastapi import UploadFile
from storage3.utils import StorageException

def get_foods():
    res = supabase.table("foods").select(
        """*, products:food_products (amount, product:product_id (id, name))""").execute()
    return res.data


def get_food_by_id(food_id: int):
    res = supabase.table("foods").select(
        "*, products:food_products (amount, product:product_id (id, name))").eq("id", food_id).execute()
    return res.data


def upsert_food(data):
    try:
        res = supabase.table("foods").upsert(data).execute()
        return res.data
    except Exception as ex:
        raise ex


def upload_file(file: UploadFile, food: str, number: int):
    try:
        path = f"foods/{food}-{number}.{file.filename.split('.')[-1]}"
        file.file.seek(0)
        file_bytes = file.file.read()
        content_type = file.content_type

        # Intenta subir el archivo primero
        res = supabase.storage.from_("images").upload(
            path, file_bytes, file_options={"content-type": content_type})

        # Verifica si hay algún otro tipo de error
        if res.status_code != 200:
            raise Exception(res)

        file.file.close()
        return res.status_code  # O considera devolver res.status_code si es relevante para tu lógica
    except StorageException as ex:
        res = supabase.storage.from_("images").update(
            path, file_bytes, file_options={"content-type": content_type})

        # Verifica si hay algún otro tipo de error
        if res.status_code != 200:
            raise Exception(res)

        file.file.close()
        return res.status_code
    except Exception as ex:
        raise ex


def get_images_from_food(food: str):
    try:
        # Listar todos los archivos en el directorio específico
        prefix = f"foods/{food}"
        list_response = supabase.storage.from_(
            "images").list("foods/", options={"limit": 50})

        if not list_response:
            return []

        # Filtrar archivos por un criterio específico, en este caso, por prefijo
        files = [
            file for file in list_response if file["name"].startswith(food)]

        # Obtener la URL pública para cada archivo filtrado
        urls = []
        for file in files:
            url_response = supabase.storage.from_(
                "images").get_public_url(file["name"])
            if not url_response:
                raise Exception(
                    "Error al obtener la URL pública", url_response)
            urls.append(url_response.removesuffix(
                '?').replace("/images/", "/images/foods/"))

            print(urls)

        return urls
    except Exception as ex:
        raise ex
