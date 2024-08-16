from fastapi import FastAPI
from .database import engine, Base
from .routes import products, orders, users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(users.router)
