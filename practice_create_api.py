from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import json

class DATA(BaseModel):
    name:str
    price:int
    
class DATA1(BaseModel):
    name:str
    price:int
    
app = FastAPI()
with open('file1.json','r') as f:
    read_file1 = json.load(f)
    
@app.get('/')
def get_data():
    return read_file1

@app.post('/postd/')
def post_data(data:DATA):
    read_file1.append(data)
    return read_file1

@app.put('/putd/{put_price}')
def put_data(put_price:str,data:DATA):
    for i , values in enumerate(read_file1):
        if values['name'] == put_price:
            read_file1[i] = DATA1.dict()
            return read_file1
    raise HTTPException(status_code=404,detail='put error')
    
@app.patch('/patchd/{patch_name}')
def patch_data(patch_name:str,data:DATA):
    for i , values in enumerate(read_file1):
        if values['name'] == patch_name:
            values['price'] = data.price
            return read_file1
    raise HTTPException(status_code=404,detail='put error')
        
@app.delete('/deleted/{delete_name}')
def delete_data(delete_name:str):
    for i, values in enumerate(read_file1):
        if values['name'] == delete_name:
            del read_file1[i]
            return read_file1
    raise HTTPException(status_code=404,detail='put error')
    
