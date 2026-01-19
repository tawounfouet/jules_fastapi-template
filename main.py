from fastapi import FastAPI
from config.database import engine
from models.base import Base
# Ensure models are imported so they are registered with Base
from models import user, post, comment
from routers import users, auth, blog, comments

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pragmatic Layered Architecture")

app.include_router(auth.router, prefix="/auth")
app.include_router(users.router)
app.include_router(blog.router)
app.include_router(comments.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Layered Architecture API"}
