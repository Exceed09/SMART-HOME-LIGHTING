from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(".env")


DATABASE_NAME = "exceed09"
COLLECTION_NAME = "SMART_HOME_LIGHTING"
USERNAME = os.getenv('name')
PASSWORD = os.getenv('password')
MONGO_KU_SERVER_URL = f"mongodb://{USERNAME}:{PASSWORD}@mongo.exceed19.online:8443/?authMechanism=DEFAULT"

router = APIRouter(
    prefix="/exceed09/mode",
    tags=["mode"]
)

client = MongoClient(MONGO_KU_SERVER_URL)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]


@router.put("/{room_id}/{mode_auto}")
def change_mode(room_id: int, mode_auto: bool):
    if not (0 < room_id < 4):
        raise HTTPException(404, detail="room id not in range.")
    collection.update_one({"room_id": room_id}, {"$set": {"mode_auto": mode_auto, "is_change": True}})
    result = collection.find({})
    list_result = []
    for room in result:
        list_result.append({"room_id": room['room_id'],
                            "mode_auto": room['mode_auto'],
                            "on_status": room['on_status'],
                            "brightness": room['brightness']})
    return {"message": list_result}
