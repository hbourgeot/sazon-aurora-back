from fastapi import APIRouter, HTTPException
from app.schemas import Provider
from app.supabase.functions.providers import upsert_provider, get_providers, get_provider_by_id

provs = APIRouter()


# Routes
@provs.get("/all")
def get_provs():
    res = get_providers()
    return res


@provs.post("/new")
def create_prov(prov: Provider):

    provider_dict = prov.model_dump()
    provider = upsert_provider(provider_dict)
    if provider is None:
        raise HTTPException(status_code=500, detail="Provider error")

    return {"provider": True}, 200

@provs.put("/{prov_id}")
def update_prov(prov_id: int, prov: Provider):
    provider_dict = prov.model_dump()
    
    exists_in_db = get_provider_by_id(prov_id)
    if exists_in_db is None:
        raise HTTPException(status_code=404, detail="Provider not found")
    
    provider_dict["id"] = prov_id
    prov_response = upsert_provider(provider_dict)
    if prov_response is None:
        raise HTTPException(status_code=500, detail="Provider error")
    
    return {"provider": True}, 200