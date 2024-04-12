from fastapi import FastAPI
from typing import Optional

fast_api=FastAPI()
@fast_api.get('/clients/')
def client_details(limit: int):
    return {"clients":" {} client details available".format(limit)}

@fast_api.get('/clients1/')
def client_details1(limit: int=1000): 
    return {"clients":" {} client details available".format(limit)}

@fast_api.get('/clients2/')
def client_details2(limit:int=10,active:bool=True):
    return {"clients":"{} client details available".format(limit),"active":active}

@fast_api.get('/clients3/')
def client_details2(limit:int=10,active:bool=True,python:Optional[str]=None):
    return {"clients":"{} client details available".format(limit),"active":active,"python":python}

@fast_api.get('/clients4/')
def client_details2(limit:int=10,active:bool=True,python:Optional[str]=None,skip:int=2):
    return {"clients":"{} client details available".format(limit),"active":active,"python":python,"skipped":skip}

@fast_api.get('/clients5/')
def client_details2(youtube:str,limit:int=10,active:bool=True,python:Optional[str]=None,skip:int=2):
    return {"clients":"{} client details available".format(limit),"active":active,"python":python,"skipped":skip,"youtube":youtube}