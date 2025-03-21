from fastapi import FastAPI
import requests
import datetime



app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/coins/currency1/currency2")
def excahnge(currency1: str, currency2: str):
    response = requests.get(f"https://economia.awesomeapi.com.br/json/last/:moedas/{currency1}-{currency2}")
    compra = response.json()[f"{currency1}{currency2}"]["bid"]
    venda = response.json()[f"{currency1}{currency2}"]["ask"]
    resposta = {
    "sell": venda,
    "buy": compra,
    "date": datetime.datetime.now() ,
    "id-account": ""
    }
    return resposta
    
