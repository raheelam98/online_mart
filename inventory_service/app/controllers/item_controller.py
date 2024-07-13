from fastapi import  HTTPException
from sqlmodel import Session, select

from app.db.db_connector import  DB_SESSION

from app.models.item_model import Item, ItemModel, ItemUpdateModel, ItemDetail


### ============================================================================================================= ###

def get_item_from_db(session: DB_SESSION):
    item = session.exec(select(Item)).all() 
    if not item:
        HTTPException(status_code=400, detail="Not found")
    return item 

### ============================================================================================================= ###

# Function to add data into database
def add_item_in_db(item_form: ItemDetail, session: DB_SESSION):
    
    # Convert ItemModel to item instance
    item = Item(**item_form.model_dump())

    if not item:
        raise HTTPException(status_code=404, detail="Not Found")
    # Add the data to the session
    session.add(item)
    # Commit the session to save the data to the database
    session.commit()
    # Refresh the session to retrieve the new data, including generated fields like _id
    session.refresh(item)
    # Return the created item
    return item

### ============================================================================================================= ###

def update_item_in_db(selected_id: int, item_form: ItemUpdateModel, session: DB_SESSION):
    # Construct a statement to select the item with the specified _id
    item_statement = select(Item).where(Item.item_id == selected_id)
    
    # Execute the statement and get the first result
    item = session.exec(item_statement).first()
    
    # If no item is found with the given ID, raise a 404 HTTPException
    if not item:
        raise HTTPException(status_code=404, detail="Not Found")
    
    # Update the fields of the item with the values from the item_form object

    if item_form.item_name is not None:
        item.item_name = item_form.item_name
    if item_form.item_quantity is not None:
        item.item_quantity = item_form.item_quantity
    if item_form.item_price is not None:
        item.item_price = item_form.item_price
    # if item_form.item_size is not None:
    #     item.item_size = item_form.item_size
    
    # Add the updated item instance to the session
    session.add(item)
    
    # Commit the transaction to save changes to the database
    session.commit()
    
    # Refresh the session to get the updated item instance
    session.refresh(item)
    
    # Return the updated item instance
    return item


### ============================================================================================================= ###
### ============================================================================================================= ###
### ============================================================================================================= ###
