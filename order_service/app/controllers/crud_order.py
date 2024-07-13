from fastapi import  HTTPException
from sqlmodel import Session, select

from app.db.db_connector import  DB_SESSION

from app.models.order_model import Order, OrderModel, OrderDetail



### ============================================================================================================= ###

def get_order_from_db(session: DB_SESSION):
    order = session.exec(select(Order)).all() 
    if not order:
        HTTPException(status_code=400, detail="Note found")
    return order 

### ============================================================================================================= ###

# Function to add data into database
def add_order_in_db(order_form: OrderDetail, session: DB_SESSION):
    
    # Convert OrderModel to order instance
    order = Order(**order_form.model_dump())

    if not order:
        raise HTTPException(status_code=404, detail="Product Not Found")
    # Add the order to the session
    session.add(order)
    # Commit the session to save the order to the database
    session.commit()
    # Refresh the session to retrieve the new order data, including generated fields like _id
    session.refresh(order)
    # Return the created order
    return order

### ============================================================================================================= ###


def update_order_in_db(selected_id: int, order_form: OrderModel, session: DB_SESSION):
    # Construct a statement to select the order with the specified _id
    order_statement = select(Order).where(Order.order_id == selected_id)
    
    # Execute the statement and get the first result
    order = session.exec(order_statement).first()
    
    # If no order is found with the given ID, raise a 404 HTTPException
    if not order:
        raise HTTPException(status_code=404, detail="Not Found")
    
    # Update the fields of the order with the values from the order_form object

    if order.order_quantity is not None:
        order.order_quantity = order_form.order_quantity
    if order.advance_payment is not None:
        order.advance_payment = order_form.advance_payment
    if order.total_price is not None:
        order.total_price = order_form.total_price
    if order.deliver_date is not None:
        order.deliver_date = order_form.deliver_date

    # if order.order_quantity is not None:
    #     order.order_quantity = order_form.order_quantity
              
        
    # Add the updated order instance to the session
    session.add(order)
    
    # Commit the transaction to save changes to the database
    session.commit()
    
    # Refresh the session to get the updated order instance
    session.refresh(order)
    
    # Return the updated order instance
    return order