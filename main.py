from fastapi import FastAPI
from app.api import ingest
from app.websocket.manager import sio
from socketio import ASGIApp

app = FastAPI(title="AROGYA")
app.include_router(ingest.router, prefix="/api")

# wrap FastAPI with Socket.IO
application = ASGIApp(sio, app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:application", host="0.0.0.0", port=8000, reload=True)
