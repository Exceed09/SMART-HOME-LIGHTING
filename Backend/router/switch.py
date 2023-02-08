from fastapi import APIRouter, Body, HTTPException
from typing import Union, Optional
from pydantic import BaseModel
from dotenv import load_dotenv
from os import getenv
from pymongo import MongoClient

router = APIRouter(
    prefix="/switch",
    tags=["switch"]
)

DATABASE_NAME = "exceed09"
COLLECTION_NAME = "SMART_HOME_LIGHTING"
MONGO_DB_DOM = "mongo.exceed19.online"
MONGO_DB_PORT = 8443

load_dotenv(".env")
username = getenv("username")
password = getenv("password")

client = MongoClient(f"mongodb://{username}:{password}@{MONGO_DB_DOM}:{MONGO_DB_PORT}/?authMechanism=DEFAULT")

db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

@router.put("/{room_id}/{on_status}")
def switch_on_off(room_id: int, on_status: bool):
    if not (0<room_id<4):
        raise HTTPException(404, detail="Invalid Value")
    collection.update_one({"room_id": room_id}, update={"$set": {"on_status": on_status, "is_change": True}})
    result = list()
    for room in collection.find({}):
        result.append({
            "room_id": room["room_id"],
            "mode_auto": room["mode_auto"],
            "on_status": room["on_status"],
            "brightness": room["brightness"],
        })
    return {"message": result}