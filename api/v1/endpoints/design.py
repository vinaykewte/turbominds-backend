from uuid import uuid4
from fastapi import APIRouter, HTTPException, Path
from schemas.design import GenerateDesign
from services.design import generate_design
from pydantic import UUID4

router = APIRouter(tags=['design'])

@router.post("")
async def create_design(data: GenerateDesign):
    print("Designing...", data)
    res = generate_design(data)
    return res


