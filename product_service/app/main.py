from fastapi import FastAPI , HTTPException, Depends
from typing import Annotated

from app.db.db_connector import create_db_and_tables,DB_SESSION
from app.controllers.crud_product import get_product_from_db ,  add_product_in_db, update_product_in_db
from app.models.product_model import Product , ProductModel , ProductUpdateModel, ProductDetail

from app.models.categories_model import Category, CategoryModel, Size, SizeModel
from app.controllers.crud_category import ( add_category_in_db, get_category_from_db, update_category_in_db
                                           , add_size_in_db, get_size_from_db, update_size_in_db )

### ============================================================================================================= ###


app = FastAPI(lifespan = create_db_and_tables)

@app.get('/')
def get_route():
    return "product service"

### ============================================================================================================= ###

@app.get('/api/product', response_model=list[Product])
def get_product(session:DB_SESSION):
      product_list = get_product_from_db(session)
      if not product_list:
        raise HTTPException(status_code=404, detail="Product Not Found in DB")
      else:
        return product_list    
      
### ============================================================================================================= ###



@app.post("/api/add_product", response_model=Product)
def add_product(new_product: ProductDetail, session: DB_SESSION ):
    # Call the function to add the data to the database
    created_product = add_product_in_db(new_product, session)
    if not created_product:
        raise HTTPException(status_code=404, detail="Can't Add Product")
    return created_product

### ============================================================================================================= ###

@app.put('/api/update_product', response_model=Product)
def update_product(id: int, product_detail: ProductUpdateModel, session: DB_SESSION):
    # Call the function to update the data to the database
    updated_product = update_product_in_db(id, product_detail, session)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Can't Find Product")
    return updated_product

### ============================================================================================================= ###
### ============================================================================================================= ###
### ============================================================================================================= ###

@app.get('/api/category', response_model=list[Category])
def get_category(session:DB_SESSION):
      category_list = get_category_from_db(session)
      if not category_list:
        raise HTTPException(status_code=404, detail="Not Found")
      else:
        return category_list   
      
### ============================================================================================================= ###

      
@app.post('/api/add_category', response_model=Category)
def create_category(category_form: CategoryModel, session: DB_SESSION):
    created_category = add_category_in_db(category_form, session)
    if not create_category:
        raise HTTPException(status_code=404, detail="Not Found")
    return created_category      

### ============================================================================================================= ###

@app.put('/api/update_category/{id}', response_model=Category)
def update_category(id: int, category_detail: CategoryModel, session: DB_SESSION):
    updated_category = update_category_in_db(id, category_detail, session)
    if not update_category:
        raise HTTPException(status_code=404, detail="Not Found")
    return updated_category

### ============================================================================================================= ###
### ============================================================================================================= ###
### ============================================================================================================= ###

@app.get('/api/size', response_model=list[Size])
def get_size(session:DB_SESSION):
      size_list = get_size_from_db(session)
      if not size_list:
        raise HTTPException(status_code=404, detail="Not Found")
      else:
        return size_list   
      
### ============================================================================================================= ###

@app.post('/api/add_size', response_model=Size)
def create_size(size_form: SizeModel, session: DB_SESSION):
    created_size = add_size_in_db(size_form, session)
    if not created_size:
        raise HTTPException(status_code=404, detail="Not Found")
    return created_size

### ============================================================================================================= ###



@app.put('/api/update_size/{id}', response_model=Size)
def update_size(id: int, size_detail: SizeModel, session:  DB_SESSION):
    updated_size = update_size_in_db(id, size_detail, session)
    if not updated_size:
        raise HTTPException(status_code=404, detail="Not Found")
    return updated_size


### ============================================================================================================= ###
### ============================================================================================================= ###
### ============================================================================================================= ###
### ============================================================================================================= ###
