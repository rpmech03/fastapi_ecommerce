from typing import List, Optional
import uuid
from pydantic import BaseModel

class categoryitem(BaseModel):
    name:str
    description: str


class subcategoryitem(BaseModel):
    category_id: int
    name: str
    description: str

class productitem(BaseModel):
    category_id: int
    subcategory_id: int
    product_name: str
    brand: str
    selling_price: int
    discount_price: int
    description: str

class categoryDelete(BaseModel):
     category_id: int

class categoryUpdate(BaseModel):
    id:int
    name:str
    description:str  

#admin registration
class Useradmin(BaseModel):
    email:str
    Full_name: str
    mobile:str
    password:str

#use for login token
class Token(BaseModel):
    access_token : str
    token_type : str = 'bearer'

class AdminLogin(BaseModel):
    email:str
    password:str