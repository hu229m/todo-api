# Todo API
Et REST API for å håndere en gjøremålsliste, bygget med FastAPI (Python). Dataene ligers i en JSON-fil slik at de huskes mellom omstarter.
## Kom i gang 
installer avhengigheter: 
pip install fastapi uvicorn
Start serveren:
uvicorn main:app -- reload
## Endepunkter 

### GET /todos
Henter alle oppgaver 

### POST /todos
legger til en ny oppgaver.

### PUT /todos/{id}
Oppdaterer en eksisterende oppgave.

### DELETE /todos/{id}
Sletter en oppgave.

## Interaktiv dokumentasjon
Åpne i nettleseren når serveren kjører:

http://localhost:8000/docs

## Datalagring 
oppgavene lagres automatisk i data/todos.json