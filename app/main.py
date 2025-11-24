from fastapi import FastAPI, HTTPException

app = FastAPI()

# Banco de dados fictício
items_db = {
    1: {"id": 1, "nome": "Item 1"},
    2: {"id": 2, "nome": "Item 2"},
}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id in items_db:
        return items_db[item_id]
    raise HTTPException(status_code=404, detail="Item não existe")
