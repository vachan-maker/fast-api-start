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


# create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message":"Todo has been added"}
# Get a todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo":todo}
    return {"message":"Todo not found"}
# Update a todo

# Delete a todo