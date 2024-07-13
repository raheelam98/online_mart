from datetime import datetime, timezone
from typing import List, Literal, Optional
import uuid
from sqlmodel import Field, Relationship, SQLModel

### ============================================================================================================= ###

class User(SQLModel, table=True):
    user_id: Optional[int] = Field(None, primary_key=True)
    user_email: str
    user_name: str
    country: str
    address: str = Field(max_length=60)
    phone_number: int

### ============================================================================================================= ###

class Item(SQLModel, table=True):
    item_id : int | None = Field(default=None, primary_key=True)
    item_name : str
    item_quantity : int 
    item_price : float
    item_size : str

### ============================================================================================================= ###

class OrderBase(SQLModel):
     order_date: datetime = Field(default=datetime.now(timezone.utc))


class OrderDetail(SQLModel):
    order_quantity: int = Field(default=1)  # (at leat one item)
    advance_payment: Optional[float]
    total_price: float
    order_type: str = Field(default="normal")   # (urgent , normal)
    order_status: str = Field(default="processing")  # (processing, complete, despatch, pending, cancelled, refund)
    order_address: str = Field(max_length=60)
    deliver_date : datetime = Field(default=datetime.now())

    product_id : int = Field(int, foreign_key="product.product_id")
    user_id : int = Field(int, foreign_key="user.user_id")
    item_id : int = Field(int, foreign_key="item.item_id")

class OrderModel(OrderBase, OrderDetail):
    pass

class Order(OrderModel, table=True):
    order_id: Optional[int] = Field(default=None, primary_key=True)

### ============================================================================================================= ###

class Product(SQLModel, table=True):
    product_id: Optional[int] = Field(None, primary_key=True)
    product_name: str
    product_type: str 
    product_price : float
    advance_payment_percetage: float = Field(default=0)
    category_id : int = Field(foreign_key="category.category_id")
    size_id : int = Field(foreign_key="size.size_id")

### ============================================================================================================= ###

class CategoryModel(SQLModel):
    category_name: str    

class Category(CategoryModel, table=True):
    category_id: Optional[int] = Field(None, primary_key=True)


### ============================================================================================================= ###

class SizeModel(SQLModel):
    size: str  # (Large, Medium, Small)    

class Size(SizeModel, table=True):
    size_id: Optional[int] = Field(default=None, primary_key=True)


### ============================================================================================================= ###




















    #items: List["OrderItem"] = Relationship(back_populates="order")

### ============================================================================================================= ###

# class OrderItem(OrderItemBase, table=True):
#     order_item_id: Optional[int] = Field(default=None, primary_key=True)
#     order_id: int = Field(foreign_key="order.order_id")
#     order: Optional[Order] = Relationship(back_populates="items")

### ============================================================================================================= ###

# class ProductSize(SQLModel, table=True):
#     product_size_id: Optional[int] = Field(None, primary_key=True)
#     size_id: int = Field(foreign_key="size.size_id")
#     price: int = Field(gt=0)  # Price associated with this size
#     product_item_id: int= Field(foreign_key="productitem.item_id")
#     # One-to-one relationship with Stock
#     stock: "Stock" = Relationship(back_populates="product_size")
#     product_item: Optional["ProductItem"] = Relationship(
#         back_populates="sizes"
#     )  # Many-to-one relationship with ProductItem


### ============================================================================================================= ###

# class Product(SQLModel, table=True):

#     product_id: Optional[int] = Field(
#         default=None, primary_key=True)  # Primary key for Product
#     product_name: str  # Name of the product
#     product_description: str  # Description of the product
#     product_type: str
#     advance_payment_percentage: float = Field(default=0)
#     category_id: int = Field(foreign_key="category.category_id")
#     # product_items: List["ProductItem"] = Relationship(
#     #     back_populates="product")  # One-to-many relationship with ProductItem


### ============================================================================================================= ###

# class ProductItem(SQLModel, table=True):

#     item_id: Optional[int] = Field(
#         default=None, primary_key=True)  # Primary key for ProductItem
#     # Foreign key linking to Product
#     product_id: int = Field(foreign_key="product.product_id")
#     color: str
#     # Many-to-one relationship with Product
#     product: Optional[Product] = Relationship(back_populates="product_items")
#     # One-to-many relationship with ProductSize
#     sizes: List[ProductSize] = Relationship(back_populates="product_item")

### ============================================================================================================= ###

# class Stock(SQLModel, table=True):
#     stock_id: Optional[int] = Field(
#         default=None, primary_key=True)  # Primary key for Stock
#     product_size_id: int = Field(foreign_key="productsize.product_size_id")
#     stock: int = 0  # Stock level
#     product_size: Optional[ProductSize] = Relationship(
#         back_populates="stock")  # One-to-one relationship with ProductSize   

### ============================================================================================================= ###

### ============================================================================================================= ###

### ============================================================================================================= ###








### ============================================================================================================= ###

### ============================================================================================================= ###

### ============================================================================================================= ###

### ============================================================================================================= ###

### ============================================================================================================= ###


