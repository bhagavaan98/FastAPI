from fastapi import FastAPI
app=FastAPI() # object name we can take any name
@app.get('/')  #this is router
def home():
    return {"name":"bhagavaan","age":25}

@app.get("/items/")  
def list_items():
    return {"car":["XUV","shift","i10"],"engine_type":"petrol"}

# how to send values dynamically
@app.get("/items/{item_id}")
def list_items(item_id:int):
    return {"id":item_id,"car":["XUV","shift","i10"],"engine_type":"petrol"}