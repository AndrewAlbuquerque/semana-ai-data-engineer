from pydantic import BaseModel, Field, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional, Literal
from decimal import Decimal

class Customer(BaseModel):
    customer_id: UUID
    name: str
    email: EmailStr
    city: Optional[str] = None
    state: Optional[str] = Field(None, min_length=2, max_length=2)
    segment: Literal['premium', 'standard', 'basic']

class Product(BaseModel):
    product_id: UUID
    name: str
    category: Optional[str] = None
    price: Decimal
    brand: Optional[str] = None

class Order(BaseModel):
    order_id: UUID
    customer_id: UUID
    product_id: UUID
    qty: int = Field(..., ge=1, le=10)
    total: Decimal = Field(..., ge=0)
    status: Literal['delivered', 'shipped', 'processing', 'cancelled']
    payment: Literal['pix', 'credit_card', 'boleto']
    created_at: datetime = Field(default_factory=datetime.now)

class Review(BaseModel):
    review_id: UUID
    order_id: UUID
    rating: int = Field(..., ge=1, le=5)
    comment: str
    sentiment: Literal['positive', 'neutral', 'negative']

class ReviewAnalysis(BaseModel):
    summary: str
    overall_sentiment: Literal['positive', 'neutral', 'negative']
    top_complaints: list[str]
    is_critical: bool
