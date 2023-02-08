from fastapi import APIRouter, Body, HTTPException
from typing import Union, Optional
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import urllib

load_dotenv('/Users/tharunthornmusik/Documents/CodeSpace/KU/ExceedCamp/Mongo/.env')

user = os.getenv('username')
password =  os.getenv('password')
client = MongoClient(f'mongodb://{user}:{password}@mongo.exceed19.online:8443/?authMechanism=DEFAULT')

db = client["exceed09"]
collection = db["SMART_HOME_LIGHTING"]

router = APIRouter(
    prefix="/brightness",
    tags=["brightness"]
)

@router.put("/{room_id}/{brightness}")
def get_brightness_change(room_id : int, brightness : int):
    if not (room_id < 1 or room_id > 4) and not (brightness < 1 or brightness > 255):
        collection.update_one({"room_id":room_id}, {"$set":{"brightness":brightness, "is_change": True}})
        room = list(collection.find({"room_id": room_id}))[0]
        return {"room_id": room["room_id"], "brightness": room["brightness"], "is_change": room["is_change"]}
    if room_id < 1 or room_id > 4:
        return HTTPException(status_code=404, detail="Room not found")
    if brightness < 1 or brightness > 255:
        return HTTPException(status_code=404, detail="Brightness invalid")
    else:
        return HTTPException(status_code=400, detail="Bad request")
