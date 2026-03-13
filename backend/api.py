from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel, field_validator
from pathlib import Path
import os
import threading
from core.train_logic import run_training

router = APIRouter()

# === 安全配置 ===
API_TOKEN = os.getenv("API_TOKEN", "flyvis-secret")  # 默认密码，建议启动时改
MODEL_DIR = Path("models").resolve()
MAX_TIMESTEPS = 500_000
MIN_TIMESTEPS = 100

def verify_token(authorization: str = Header(...)):
    if not authorization or authorization.replace("Bearer ", "") != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid or missing token")

class TrainRequest(BaseModel):
    timesteps: int = 10000
    model_name: str = "ppo_fly_final.zip"  # 只接受文件名，不接受路径！

    @field_validator('timesteps')
    @classmethod
    def check_timesteps(cls, v):
        if v < MIN_TIMESTEPS or v > MAX_TIMESTEPS:
            raise ValueError(f'timesteps must be between {MIN_TIMESTEPS} and {MAX_TIMESTEPS}')
        return v

    @field_validator('model_name')
    @classmethod
    def check_model_name(cls, v):
        if not v.endswith('.zip'):
            raise ValueError('Model name must end with .zip')
        if any(c in v for c in ['/', '\\', '..']):
            raise ValueError('Invalid characters in model name')
        return v

@router.post("/train", dependencies=[Depends(verify_token)])
def train_model(request: TrainRequest):
    try:
        MODEL_DIR.mkdir(exist_ok=True)
        model_path = MODEL_DIR / request.model_name

        thread = threading.Thread(
            target=run_training,
            kwargs={"timesteps": request.timesteps, "model_path": str(model_path)}
        )
        thread.start()
        return {"message": "训练已启动", "timesteps": request.timesteps}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
def health():
    return {"status": "OK"}