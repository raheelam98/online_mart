from datetime import datetime
from typing import Literal, Optional
from sqlmodel import Relationship, SQLModel, Field 
from datetime import timedelta, timezone
   
### ============================================================================================================= ###

class StockModel(SQLModel):
    stock_number : int = 0
    stock_available : bool = Field(default=False)   
    # stock_level: Literal["Low", "Medium", "High"] = "High" if stock> 100 else "Medium" if stock >50 else "Low"
    
    item_id : int = Field(int, foreign_key="item.item_id")
    size_id: int = Field(int, foreign_key='size.size_id')

class Stock(StockModel, table=True):
    stock_id: int | None= Field(default=None, primary_key=True)

    #product_id: int = Field(int, foreign_key="product.product_id")

### ============================================================================================================= ###

class ItemBase(SQLModel):
    item_add_date : datetime = Field(default=datetime.now(timezone.utc))
    ##item_date : datetime = Field(default=datetime.now())


class ItemDetail(SQLModel):
    item_name : str
    item_quantity : int 
    item_price : float
    item_demand : str # ["Maximum", "Average", "Minimum]
    item_size : str
    vender_name : str

    category_id : int = Field(int, foreign_key="category.category_id")
    product_id : int = Field(int, foreign_key="product.product_id")

class ItemModel(ItemBase, ItemDetail):
    pass    
    
class Item(ItemModel, table=True):
    item_id : int | None = Field(default=None, primary_key=True)

class ItemUpdateModel(SQLModel):
    item_name: Optional[str]
    item_quantity: Optional[str]
    item_price: Optional[int]
    item_size: Optional[str]
    vender_name: Optional[str]    

### ============================================================================================================= ###

class Product(SQLModel, table=True):
    product_id: Optional[int] = Field(default=None, primary_key=True)
    product_name: str
    product_description: str | None
    product_price: float
   
### ============================================================================================================= ###

class Category(SQLModel, table=True):
    category_id: Optional[int] = Field(None, primary_key=True)
    category_name: str

### ============================================================================================================= ###

class Size(SQLModel, table=True):
    size_id: Optional[int] = Field(default=None, primary_key=True)
    size: str  # (Large, Medium, Small)














### ============================================================================================================= ###


# class OrderModel(SQLModel):
#     order_quantity: int = Field(default=1)  # (at leat one item)
#     advance_price: Optional[float]
#     total_price: float
#     order_type: str
#     order_status: str = Field(default="processing")  # (processing, complete, despatch, pending, cancelled, refund)
#     order_date: datetime = Field(default=datetime.now(timezone.utc))
    
#     product_id : int = Field(int, foreign_key="product.product_id")
#     user_id : int = Field(int, foreign_key="user.user_id")


# class Order(OrderModel, table=True):
#     order_id: Optional[int] = Field(default=None, primary_key=True)



# class Order(SQLModel, table=True):
#     order_id: int | None = Field(int, primary_key=True)
#     quantity: int = Field(default=1)  # (at leat one item)
#     created_date : datetime = Field(default=datetime.now())
#     deliver_date : datetime = Field(default=datetime.now())
#     total_price: float
#     order_status: str = Field(default="processing")  # (processing, complete, despatch, pending, cancelled, refund)
    
#     user_id: int = Field(int, foreign_key="user.user_id")
#     product_id: int = Field(int, foreign_key="product.product_id")
#     item_id : int = Field(int, foreign_key="item.item_id")

### ============================================================================================================= ###

    # @property
    # def stock_level(self) -> Literal["Low", "Average", "High"]:
    #     if self.stock > 100:
    #         return "High"
    #     elif self.stock > 50:
    #         return "Average"
    #     else:
    #         return "Low"