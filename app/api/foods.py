from fastapi import APIRouter

foods = APIRouter()


# Routes
@foods.get("/all")
def get_foods():
    return {"take": []}


@foods.get("/{id}")
def get_food(id: int):
    return {"take":id}


@foods.post("/new")
def create_food():
    return {"message": "Hey"}

@foods.put("/{id}")
def update_food(id: int):
    return {"message": "up"}