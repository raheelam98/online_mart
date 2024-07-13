from fastapi import  HTTPException
from sqlmodel import Session, select

from app.db.db_connector import  DB_SESSION

from app.models.product_model import Product, ProductModel, ProductUpdateModel, ProductDetail


### ============================================================================================================= ###

def get_product_from_db(session: DB_SESSION):
    porduct = session.exec(select(Product)).all() 
    if not porduct:
        HTTPException(status_code=400, detail="Product not found")
    return porduct 

### ============================================================================================================= ###

# # Function to add data into database
# def add_product_in_db(product_form: ProductModel, session: DB_SESSION):
    
#     # Convert ProductModel to product instance
#     #product = Product(**product_form.model_dump())
#     product = Product(**product_form.dict())
#     print('Product 1....', product)

#     if not product:
#         raise HTTPException(status_code=404, detail="Product Not Found")
#     # Add the product to the session
#     session.add(product)
#     # Commit the session to save the product to the database
#     session.commit()
#     # Refresh the session to retrieve the new product data, including generated fields like product_id
#     session.refresh(product)
#     # Return the created product
#     print('Product end....', product)
#     return product

def add_product_in_db(product_form: ProductDetail, session: Session):
    # Convert ProductModel to Product instance
    #product = Product(**product_form.dict())
    product = Product(**product_form.model_dump())

    print('Product ....1')
    if not product:
        raise HTTPException(status_code=404, detail="Product Not Found")
    

    # Add the product to the session
    session.add(product)
    # Commit the session to save the product to the database
    session.commit()
    # Refresh the session to retrieve the new product data, including generated fields like product_id
    session.refresh(product)
    # Return the created product
    print('Product end....', product)
    return product

### ============================================================================================================= ###


def update_product_in_db(selected_id: int, product_form: ProductUpdateModel, session: DB_SESSION):
    # Construct a query to select the product with the specified product_id
    product_query = select(Product).where(Product.product_id == selected_id)
    
    # Execute the query and get the first result
    product_statment = session.exec(product_query).first()
    
    # If no product is found with the given ID, raise a 404 HTTPException
    if not product_statment:
        raise HTTPException(status_code=404, detail="Product is unavailable")
    
    # Update the fields of the product with the values from the product_form object
    if product_form.product_name is not None:
        product_statment.product_name = product_form.product_name
    if product_form.product_type is not None:
        product_statment.product_type = product_form.product_type
    # if product_form.product_size is not None:
    #     product_statment.product_size = product_form.product_size
    # if product_form.product_stock is not None:
    #     product_statment.product_stock = product_form.product_stock
    if product_form.product_price is not None:
        product_statment.product_price = product_form.product_price
    if product_form.is_available is not None:
        product_statment.is_available = product_form.is_available    
    if product_form.product_description is not None:
        product_statment.product_description = product_form.product_description   
    if product_form.advance_payment_percetage is not None:
        product_statment.advance_payment_percetage = product_form.advance_payment_percetage 
    

    
    # Add the updated product instance to the session
    session.add(product_statment)
    
    # Commit the transaction to save changes to the database
    session.commit()
    
    # Refresh the session to get the updated product instance
    session.refresh(product_statment)
    
    # Return the updated product instance
    return product_statment