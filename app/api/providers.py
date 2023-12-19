from fastapi import APIRouter

provs = APIRouter()


# Routes
@provs.get("/all")
def get_provs():
    return {"take": []}


@provs.get("/{id}")
def get_prov(id: int):
    return {"take":id}


@provs.post("/new")
def create_prov():
    return {"message": "Hey"}

@provs.put("/{id}")
def update_prov(id: int):
    return {"message": "up"}