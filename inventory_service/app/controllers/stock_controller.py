from fastapi import  HTTPException
from sqlmodel import Session, select

from app.db.db_connector import  DB_SESSION
from app.models.item_model import Stock, StockModel

### ============================================================================================================= ###

def get_stock_from_db(session: DB_SESSION):
    stock = session.exec(select(Stock)).all() 
    if not stock:
        HTTPException(status_code=400, detail="Not found")
    return stock 

### ============================================================================================================= ###

# Function to add data into database
def add_stock_in_db(stock_form: StockModel, session: DB_SESSION):
    
    # Convert StockModel to item instance
    stock = Stock(**stock_form.model_dump())

    if not stock:
        raise HTTPException(status_code=404, detail="Not Found")
    # Add the data to the session
    session.add(stock)
    # Commit the session to save the data to the database
    session.commit()
    # Refresh the session to retrieve the new data, including generated fields like _id
    session.refresh(stock)
    # Return the created item
    return stock

### ============================================================================================================= ###

def update_stock_in_db(selected_id: int, stock_form: StockModel, session: DB_SESSION):
    # Construct a statement to select the item with the specified _id
    stock_statement = select(Stock).where(Stock.stock_id == selected_id)
    
    # Execute the statement and get the first result
    stock = session.exec(stock_statement).first()
    
    # If no item is found with the given ID, raise a 404 HTTPException
    if not stock:
        raise HTTPException(status_code=404, detail="Not Found")
    
    # Update the fields of the stock with the values from the stock_form object

    if stock_form.stock_number is not None:
        stock.stock_number = stock_form.stock_number
    if stock_form.item_id is not None:
        stock.item_id = stock_form.item_id
    if stock_form.size_id is not None:
        stock.size_id = stock_form.size_id
    
    
    # Add the updated item instance to the session
    session.add(stock)
    
    # Commit the transaction to save changes to the database
    session.commit()
    
    # Refresh the session to get the updated stock instance
    session.refresh(stock)
    
    # Return the updated item instance
    return stock


### ============================================================================================================= ###
#