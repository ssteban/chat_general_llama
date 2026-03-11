from fastapi import FastAPI
import threading
from service.bot import bot_init


app = FastAPI()

@app.on_event("startup")
def startup():
    bot_thread = threading.Thread(target=bot_init, daemon=True)
    bot_thread.start()
    

@app.head("/head")
def health():
    return {"status": "ok"}