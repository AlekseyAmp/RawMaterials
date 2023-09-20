from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from src.config.settings import settings
from src.config.database import get_db_url

from src.routes import (
    auth as AuthRouter,
    user as UserRouter,
    material as MaterialRouter,
)


app = FastAPI(title="Raw Material Indicator API", version="0.1")


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


register_tortoise(
    app,
    db_url=get_db_url(
        user=settings.POSTGRESQL_USERNAME,
        password=settings.POSTGRESQL_PASSWORD,
        host=settings.POSTGRESQL_HOSTNAME,
        db_name=settings.POSTGRESQL_DATABASE
    ),
    modules={
        "models": [
            "src.models.material",
            "src.models.user"
        ]
    },
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
def root():
    return {
        "message": "Go to /docs"
    }


app.include_router(AuthRouter.router, tags=['auth'], prefix='/api')
app.include_router(UserRouter.router, tags=['users'], prefix='/api')
app.include_router(MaterialRouter.router, tags=['materials'], prefix='/api')
