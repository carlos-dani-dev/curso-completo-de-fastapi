from fastapi import FastAPI
from database import engine
import models
from routers import todos
from routers import auth


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)