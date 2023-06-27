from fastapi import FastAPI
from core.config import settings
from db.base import Base
from db.session import engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from apis.base import app_router


def include_router(app):
    app.include_router(app_router)


def create_table():
    Base.metadata.create_all(bind=engine)


origin = ["http://localhost:3000",
          "https://localhost:3000"]


def start_application():
    # TODO: Add openapi tags
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.add_middleware(CORSMiddleware,
                       allow_origins=origin,
                       allow_credentials=True,
                       allow_methods=["*"])
    include_router(app)
    create_table()
    return app


app = start_application()
