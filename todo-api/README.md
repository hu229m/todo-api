# Todo API

Et REST API for å håndtere en gjøremålsliste, bygget med FastAPI (Python).
Dataene lagres i en JSON-fil slik at de huskes mellom omstarter.

## Kom i gang

Installer avhengigheter:

pip install fastapi uvicorn

Start serveren:

uvicorn main:app --reload

## Endepunkter

### GET /todos
Henter alle oppgaver.

### POST /todos
Legger til en ny oppgave.

### PUT /todos/{id}
Oppdaterer en eksisterende oppgave.

### DELETE /todos/{id}
Sletter en oppgave.

## Interaktiv dokumentasjon

Åpne i nettleseren når serveren kjører:

http://localhost:8000/docs

## Datalagring

Oppgavene lagres automatisk i data/todos.json