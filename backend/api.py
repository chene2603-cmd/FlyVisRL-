from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import threading
from core.train_logic import run_training

app = FastAPI()

class TrainRequest(BaseModel):
    timesteps: int = 10000
    model_path: str = "models/ppo_fly_final.zip"

@app.post("/train")
def train_model(request: TrainRequest):
    try:
        # 确保 models 目录存在
        os.makedirs(os.path.dirname(request.model_path), exist_ok=True)
        
        # 启动训练（非阻塞）
        thread = threading.Thread(
            target=run_training,
            kwargs={
                "timesteps": request.timesteps,
                "model_path": request.model_path
            }
        )
        thread.start()
        return {"message": "训练已启动", "timesteps": request.timesteps}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "OK"}