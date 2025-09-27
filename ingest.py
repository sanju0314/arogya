from fastapi import APIRouter
from app.models.schemas import Vital
from app.ai.inference import predict_arrhythmia, predict_hypoxia
from app.websocket.manager import sio

router = APIRouter()

@router.post("/ingest")
async def ingest(v: Vital):
    alerts = []
    if predict_arrhythmia(v.ecg):      alerts.append("Arrhythmia")
    if predict_hypoxia(v.spo2, v.hr):  alerts.append("Hypoxia")
    if v.temp >= 38.0:                 alerts.append("Fever")
    if v.fall:                         alerts.append("Fall")

    # broadcast to every connected dashboard
    await sio.emit("vitals", {**v.dict(), "alerts": alerts})
    return {"status": "ok", "alerts": alerts}
