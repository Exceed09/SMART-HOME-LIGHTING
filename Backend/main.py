from fastapi import FastAPI
from router import switch, mode, brightness, rooms
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(switch.router)
app.include_router(mode.router)
app.include_router(brightness.router)
app.include_router(rooms.router)


@app.get("/")
def root():
    return {"msg": "welcome to root page"}
