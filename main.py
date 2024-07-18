from fastapi import FastAPI
from api.v1.endpoints import brief, research, strategy

app = FastAPI()

app.include_router(brief.router, prefix="/brief", tags=["brief"])
app.include_router(research.router, prefix="/research", tags=["research"])
app.include_router(strategy.router, prefix="/strategy", tags=["strategy"])