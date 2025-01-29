from fastapi import FastAPI

app = FastAPI() 

#Endpoint Home
@app.get('/')
def home():
    return {'Hello': 'world FastAPI'}
