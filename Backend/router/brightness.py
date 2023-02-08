from fastapi import APIRouter, Body, HTTPException
from typing import Union, Optional
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import urllib

load_dotenv('.env')

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
    if not (room_id < 1 or room_id > 3) and not (brightness < 1 or brightness > 255):
        collection.update_one({"room_id":room_id}, {"$set":{"brightness":brightness, "is_change": True}})
        room = list(collection.find({"room_id": room_id}))[0]
        result = list()
        for room in collection.find({}):
            result.append({
                "room_id": room["room_id"],
                "mode_auto": room["mode_auto"],
                "on_status": room["on_status"],
                "brightness": room["brightness"],
            })
        return {"message": result} 
    if room_id < 1 or room_id > 3:
        raise HTTPException(status_code=404, detail="Room not found")
    if brightness < 1 or brightness > 255:
        raise HTTPException(status_code=404, detail="Brightness invalid")
    else:
        raise HTTPException(status_code=400, detail="Bad request")
