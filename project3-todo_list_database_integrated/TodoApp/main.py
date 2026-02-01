from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import todos, auth, admin, user


app = FastAPI()


@app.get('/healthy')
def health_check():
    return {'status': 'Healthy'}


Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(user.router)