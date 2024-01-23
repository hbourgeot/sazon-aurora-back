from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: int
    email: str
    password: str
    name: str
    role: int
    document: Optional[str] = None


class Food(BaseModel):
    id: int
    created_at: datetime
    name: str
    description: Optional[str] = None
    price: float


class Cart(BaseModel):
    id: int
    created_at: datetime
    user_id: int


class CartDetails(BaseModel):
    id: int
    cart_id: int
    food_id: int
    quantity: int
    total_price: float


class Role(BaseModel):
    id: int
    role: str


class FoodProduct(BaseModel):
    id: int
    food_id: int
    product_id: int


class Product(BaseModel):
    name: str
    description: Optional[str] = None
    stock: int
    provider_id: int


class Provider(BaseModel):
    name: str
    contact: str
    contact_type: Optional[str] = None
    address: Optional[str] = None


class Invoice(BaseModel):
    id: int
    created_at: datetime
    user_id: int
    total: float
    status: str


class InvoiceDetails(BaseModel):
    id: int
    invoice_id: int
    food_id: int
    quantity: int
    price: float

