from sqlmodel import SQLModel, Field
from typing import Optional, List, Literal
from datetime import date
import uuid

from app.models.auth_admin_model import Admin
from app.models.categories_model import Category, Size

### ============================================================================================================= ###

class ProductBase(SQLModel):
    product_code: int
    is_available: bool = False      # DEFAULT 'No',  -- yes/no
    product_description: str | None
    product_add_date : date = Field(default=date.today())
  
### ============================================================================================================= ###

class ProductDetail(SQLModel):
    product_name: str
    product_type: str 
    product_price : float
    advance_payment_percetage: float = Field(default=0)
    product_code: int
    is_available: bool = False      # DEFAULT 'No',  -- yes/no
    product_description: str | None
    category_id : int = Field(foreign_key="category.category_id")
    size_id : int = Field(foreign_key="size.size_id")
    

### ============================================================================================================= ###

class ProductModel(ProductBase, ProductDetail):
    pass

### ============================================================================================================= ###


class Product(ProductModel , table=True):
    product_id: Optional[int] = Field(default=None, primary_key=True)
    kid: str = Field(default_factory=lambda: uuid.uuid4().hex)

### ============================================================================================================= ###


class ProductUpdateModel(SQLModel):
    product_name: Optional[str]
    product_type: Optional[str]
    # product_size: Optional[str]
    # product_stock: Optional[str]
    product_price: Optional[float]
    is_available: Optional[bool]
    product_description: Optional[str]
    advance_payment_percetage: Optional[str]
  

### ============================================================================================================= ###


