from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

from app.models.order_model import Item, Product, User


class CartModel(SQLModel):
    cart_code : int 
    cart_quantity : int

    item_id : int = Field(int, foreign_key="item.item_id")
    product_id : int = Field(int, foreign_key="product.product_id")
    user_id : int = Field(int, foreign_key="user.user_id")

class Cart(CartModel, table=True):
    cart_id: Optional[int] = Field(default=None, primary_key=True)


class CartUpdateModel(SQLModel):
    cart_code: Optional[int]
    cart_quantity: Optional[int]

    item_id: Optional[int] = Field(foreign_key="item.item_id")
    product_id: Optional[int] = Field(foreign_key="product.product_id")

   
   