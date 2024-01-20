from fastapi import APIRouter, HTTPException
from app.schemas import Provider
from app.supabase.functions.providers import upsert_provider, get_providers

provs = APIRouter()


# Routes
@provs.get("/all")
def get_provs():
    res = get_providers()
    data = res.model_dump()
    return {"providers": data["data"]}


@provs.get("/{id}")
def get_prov(id: int):
    return {"take":id}


@provs.post("/new")
def create_prov(prov: Provider):

    provider_dict = prov.model_dump()
    provider = upsert_provider(provider_dict)
    if provider is None:
        raise HTTPException(status_code=500, detail="Provider error")

    return {"provider": True}, 200

@provs.put("/{id}")
def update_prov(id: int):
    return {"message": "up"}