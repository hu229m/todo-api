from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import json
import os

app = FastAPI()

DATA_FILE = "data/todos.json"

def les_todos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def skriv_todos(todos):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

class Todo(BaseModel):
    tittel: str
    ferdig: Optional[bool] = False

@app.get("/todos")
def hent_alle():
    return les_todos()

@app.post("/todos")
def legg_til(todo: Todo):
    todos = les_todos()
    ny_id = max((t["id"] for t in todos), default=0) + 1
    ny = {"id": ny_id, "tittel": todo.tittel, "ferdig": todo.ferdig}
    todos.append(ny)
    skriv_todos(todos)
    return ny

@app.put("/todos/{todo_id}")
def oppdater(todo_id: int, oppdatering: Todo):
    todos = les_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["tittel"] = oppdatering.tittel
            todo["ferdig"] = oppdatering.ferdig
            skriv_todos(todos)
            return todo
    raise HTTPException(status_code=404, detail="Ikke funnet")

@app.delete("/todos/{todo_id}")
def slett(todo_id: int):
    todos = les_todos()
    nye_todos = [t for t in todos if t["id"] != todo_id]
    if len(nye_todos) == len(todos):
        raise HTTPException(status_code=404, detail="Ikke funnet")
    skriv_todos(nye_todos)
    return {"melding": f"Oppgave {todo_id} slettet"}