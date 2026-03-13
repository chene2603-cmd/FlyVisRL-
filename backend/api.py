from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import threading
from core.train_logic import run_training

router = APIRouter()  # ← 关键：不是 FastAPI()

class TrainRequest(BaseModel):
    timesteps: int = 10000
    model_path: str = "models/ppo_fly_final.zip"

@router.post("/train")
def train_model(request: TrainRequest):
    try:
        os.makedirs(os.path.dirname(request.model_path), exist_ok=True)
        thread = threading.Thread(
            target=run_training,
            kwargs={"timesteps": request.timesteps, "model_path": request.model_path}
        )
        thread.start()
        return {"message": "训练已启动", "timesteps": request.timesteps}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
def health():
    return {"status": "OK"}
