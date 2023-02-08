from fastapi import APIRouter
from dotenv import load_dotenv
from os import getenv
from pymongo import MongoClient

router = APIRouter(
    prefix="/rooms",
    tags=["rooms"]
)

DATABASE_NAME = "exceed09"
COLLECTION_NAME = "SMART_HOME_LIGHTING"
MONGO_DB_DOM = "mongo.exceed19.online"
MONGO_DB_PORT = 8443

load_dotenv(".env")
username = getenv("name")
password = getenv("password")

client = MongoClient(f"mongodb://{username}:{password}@{MONGO_DB_DOM}:{MONGO_DB_PORT}/?authMechanism=DEFAULT")

db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]


@router.get("/")
def get_all_rooms():
    result = []
    for room in collection.find({}):
        result.append({
            "room_id": room["room_id"],
            "mode_auto": room["mode_auto"],
            "on_status": room["on_status"],
            "brightness": room["brightness"],
            "is_change": room["is_change"]
        })
    collection.update_many({}, {"$set": {"is_change": False}})
    return {"message": result}
