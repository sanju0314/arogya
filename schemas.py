from pydantic import BaseModel, Field
from datetime import datetime

class Vital(BaseModel):
    patient_id: str
    ts: datetime = Field(default_factory=datetime.utcnow)
    spo2: int
    hr: int
    temp: float
    ecg: list[float]
    ax: float
    ay: float
    az: float
    fall: bool = False
