from typing import Annotated
from fastapi import Depends, FastAPI, Body
from routers.users import router
from db.engins import engine, Base
app = FastAPI()


@app.on_event('startup')
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
app.include_router(router, prefix='/users')
