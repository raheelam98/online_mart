
from fastapi import FastAPI , HTTPException, Depends
from typing import Annotated

from app.db.db_connector import create_db_and_tables,DB_SESSION

from app.controllers.item_controller import get_item_from_db, add_item_in_db, update_item_in_db
from app.controllers.stock_controller import (get_stock_from_db, add_stock_in_db, update_stock_in_db)
                                             
from app.models.item_model import Item, ItemModel, ItemDetail, ItemUpdateModel, Stock, StockModel


### ============================================================================================================= ###
  

app = FastAPI(lifespan = create_db_and_tables)

@app.get('/')
def get_route():
    return "Inventory Service"

### ============================================================================================================= ###

@app.get('/api/item', response_model=list[Item])
def get_item(session:DB_SESSION):
      item_list = get_item_from_db(session)
      if not item_list:
        raise HTTPException(status_code=404, detail="Not Found in DB")
      else:
        return item_list    
      
### ============================================================================================================= ###

@app.post("/api/add_item", response_model=Item)
def add_item(new_item: ItemDetail, session: DB_SESSION):
    # Call the function to add the data to the database
    created_item = add_item_in_db(new_item, session)
    if not created_item:
        raise HTTPException(status_code=404, detail="Can't Add")
    return created_item

### ============================================================================================================= ###

@app.put('/api/update_item', response_model=Item)
def update_item(id: int, item_detail: ItemUpdateModel, session: DB_SESSION):
    # Call the function to update the data to the database
    updated_item = update_item_in_db(id, item_detail, session)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Can't Find Data")
    return updated_item


### ============================================================================================================= ###
### ============================================================================================================= ###
### ============================================================================================================= ###
### ============================================================================================================= ###


@app.get('/api/stock', response_model=list[Stock])
def get_item(session:DB_SESSION):
      stock_list = get_stock_from_db(session)
      if not stock_list:
        raise HTTPException(status_code=404, detail="Not Found in DB")
      else:
        return stock_list   
      
### ============================================================================================================= ###

@app.post("/api/add_stock", response_model=Stock)
def add_item(new_stock: StockModel, session: DB_SESSION):
    # Call the function to add the data to the database
    created_stock = add_stock_in_db(new_stock, session)
    if not created_stock:
        raise HTTPException(status_code=404, detail="Can't Add")
    return created_stock

### ============================================================================================================= ###

@app.put('/api/update_stock', response_model=Stock)
def update_stock(id: int, stock_detail: StockModel, session: DB_SESSION):
    # Call the function to update the data to the database
    updated_stock = update_stock_in_db(id, stock_detail, session)
    if not updated_stock:
        raise HTTPException(status_code=404, detail="Can't Find Data")
    return updated_stock


### ============================================================================================================= ###
### ============================================================================================================= ###
### ============================================================================================================= ###
### ============================================================================================================= ###
