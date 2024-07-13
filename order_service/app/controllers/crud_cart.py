from fastapi import  HTTPException
from sqlmodel import Session, select

from app.db.db_connector import  DB_SESSION
from app.models.cart_model import Cart, CartModel, CartUpdateModel

### ============================================================================================================= ###

def get_cart_from_db(session: DB_SESSION):
    cart = session.exec(select(Cart)).all() 
    if not cart:
        HTTPException(status_code=400, detail="Note found")
    return cart 

### ============================================================================================================= ###

# # Function to add data into database
def add_cart_in_db(cart_form: CartModel, session: DB_SESSION):
    
    # Convert CartModel to order instance
    cart = Cart(**cart_form.model_dump())

    if not cart:
        raise HTTPException(status_code=404, detail="Not Found")
    # Add the cart to the session
    session.add(cart)
    # Commit the session to save the cart to the database
    session.commit()
    # Refresh the session to retrieve the new cart data, including generated fields like _id
    session.refresh(cart)
    # Return the created cart
    return cart

### ============================================================================================================= ###


def update_cart_in_db(selected_id: int, cart_form: CartUpdateModel, session: DB_SESSION):
    # Construct a statement to select the cart with the specified _id
    cart_statement = select(Cart).where(Cart.cart_id == selected_id)
    print(f"update cart 1  ... {cart_statement} ")

    # Execute the statement and get the first result
    cart = session.exec(cart_statement).first()
    print(f"update cart 2  ... {cart} ")

    # If no cart is found with the given ID, raise a 404 HTTPException
    if not cart:
        raise HTTPException(status_code=404, detail="Not Found")

    print("update cart 3 ... ")
    # Update the fields of the cart with the values from the cart_form object
    if cart_form.cart_code is not None:
        cart.cart_code = cart_form.cart_code
    if cart_form.cart_quantity is not None:
        cart.cart_quantity = cart_form.cart_quantity
    if cart_form.item_id is not None:
        cart.item_id = cart_form.item_id
    if cart_form.product_id is not None:
        cart.product_id = cart_form.product_id

    # Add the updated cart instance to the session
    session.add(cart)

    # Commit the transaction to save changes to the database
    session.commit()

    # Refresh the session to get the updated cart instance
    session.refresh(cart)

    # Return the updated cart instance
    return cart

### ============================================================================================================= ###

def delete_cart_from_db(selected_id: int, session: DB_SESSION):
    cart = session.exec(select(Cart).where(
        Cart.cart_id == selected_id)).one_or_none()
    session.delete(cart)
    session.commit()
    return f"Data has been successfully deleted of this id: {selected_id}."

### ============================================================================================================= ###
