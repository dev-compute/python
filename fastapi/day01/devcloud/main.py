from typing import Annotated

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def read_root(request: Request):
    return {"message": "Hello World"}

'''
You can send requests to the /headers endpoint to see the headers sent by the client.
curl -v -X GET http://127.0.0.1:8000/headers -H "User-Agent: MyClient" -H "Accept: application/json"
curl -v -H "Host: devcloud.example.com" 127.0.0.1:8000/headers
'''
@app.get("/headers")
async def read_items(request: Request):
    for key, value in request.headers.items():
        print(f"{key}: {value}")   
    return {"Headers": dict(request.headers), "Client Host": request.client.host}   