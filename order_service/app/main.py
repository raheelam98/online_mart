from fastapi import FastAPI , HTTPException, Depends
from typing import Annotated

from app.db.db_connector import create_db_and_tables,DB_SESSION

from app.models.order_model import Order, OrderModel, OrderDetail
from app.controllers.crud_order import get_order_from_db, add_order_in_db, update_order_in_db

from app.models.cart_model import Cart, CartModel, CartUpdateModel
from app.controllers.crud_cart import get_cart_from_db, add_cart_in_db, update_cart_in_db, delete_cart_from_db

### ============================================================================================================= ###
#
app = FastAPI(lifespan = create_db_and_tables)


@app.get('/')
def get_route():
    return " service"

### ============================================================================================================= ###

@app.get('/api/order', response_model=list[Order])
def get_order(session:DB_SESSION):
      order_list = get_order_from_db(session)
      if not order_list:
        raise HTTPException(status_code=404, detail="Not Found in DB")
      else:
        return order_list    
      
### ============================================================================================================= ###


@app.post("/api/add_order", response_model=Order)
def add_order(new_order: OrderDetail, session: DB_SESSION):
    # Call the function to add the data to the database
    created_order = add_order_in_db(new_order, session)
    if not created_order:
        raise HTTPException(status_code=404, detail="Can't Add")
    return created_order

### ============================================================================================================= ###

@app.put('/api/update_order', response_model=Order)
def update_order(id: int, order_detail: OrderModel, session: DB_SESSION):
    # Call the function to update the data to the database
    updated_order = update_order_in_db(id, order_detail, session)
    if not updated_order:
        raise HTTPException(status_code=404, detail="Not Found")
    return updated_order

### ============================================================================================================= ###
### ============================================================================================================= ###
### ============================================================================================================= ###


@app.get('/api/cart', response_model=list[Cart])
def get_cart(session:DB_SESSION):
      cart_list = get_cart_from_db(session)
      if not cart_list:
        raise HTTPException(status_code=404, detail="Not Found in DB")
      else:
        return cart_list    
      
### ============================================================================================================= ###

@app.post("/api/add_cart", response_model=Cart)
def add_cart(new_cart: CartModel, session: DB_SESSION):
    # Call the function to add the data to the database
    created_cart = add_cart_in_db(new_cart, session)
    if not created_cart:
        raise HTTPException(status_code=404, detail="Can't Add")
    return created_cart

### ============================================================================================================= ###


@app.put('/api/update_cart', response_model=Cart)
def update_cart(id: int, cart_detail: CartUpdateModel, session: DB_SESSION):
    # Call the function to update the data to the database
    updated_cart = update_cart_in_db(id, cart_detail, session)
    if not updated_cart:
        raise HTTPException(status_code=404, detail="Not Found")
    return updated_cart

### ============================================================================================================= ###

@app.delete("/delete_cart", response_model=str)
def delete_cart(message: Annotated[str, Depends(delete_cart_from_db)]):
    return message

