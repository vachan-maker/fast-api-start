from fastapi import FastAPI
from models import Todo
app = FastAPI()

todos = []
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos":todos}


# Get single todos
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message":"Todo has been added"}
# Update a todo

# Delete a todo