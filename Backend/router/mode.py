from fastapi import APIRouter, Body
from typing import Union, Optional
from pydantic import BaseModel

router = APIRouter(
    prefix="/mode",
    tags=["mode"]
)


@router.put("/{modeauto}")
def change_mode(modeauto: bool):
    return {"message": "success"}
