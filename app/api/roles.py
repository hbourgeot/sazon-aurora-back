from fastapi import APIRouter, HTTPException
from app.schemas import Role
from app.supabase.functions import roles as role_table

roles = APIRouter()


# Routes
@roles.get("/all")
def get_roles():
    res = role_table.get_roles()
    roles = res.model_dump()
    return {"roles": roles}


@roles.get("/{id}")
def get_role(role_id: int):
    res = role_table.get_role_by_id(role_id)
    role = res.model_dump()
    return {"role":role}


@roles.post("/new")
def create_role(role: Role):
    try:
        role_dict = {
            "id": role.id,
            "role": role.role
        }
        result = role_table.upsert_role(role_dict)
        if result.data is not None:
            res = {"data": result.data}
        else:
            res = {"message": "Role"}
        return res
    except Exception as ex:
        return {"error": str(ex)}
