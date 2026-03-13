import os
import threading
from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse

# 👇 注意：这里假设你的训练逻辑文件在 core/train_logic.py
# 如果你的结构不同，请调整导入路径
from core.train_logic import run_training

router = APIRouter()

# 全局状态字典
training_state = {
    "status": "idle",  # 状态：idle, running, completed, failed
    "message": "",
    "model_path": "models/ppo_fly_final.zip"
}

# 🚀 启动训练 (POST /train)
@router.post("/train")
def start_training():
    if training_state["status"] == "running":
        raise HTTPException(status_code=400, detail="训练已经在运行中了")

    training_state["status"] = "running"
    training_state["message"] = "正在启动训练..."

    # 使用后台线程运行耗时的训练任务，避免阻塞 API
    def run_train():
        try:
            training_state["message"] = "开始训练..."
            run_training()  # 调用 core/train_logic.py 里的训练函数
            training_state["status"] = "completed"
            training_state["message"] = "训练成功完成！"
        except Exception as e:
            training_state["status"] = "failed"
            training_state["message"] = f"训练失败: {str(e)}"
            print(f"❌ 训练出错: {e}")

    # 启动线程
    threading.Thread(target=run_train, daemon=True).start()

    return {"message": "训练任务已提交", "status": training_state["status"]}

# 🔍 查看状态 (GET /status)
@router.get("/status")
def get_status():
    return {
        "status": training_state["status"],
        "message": training_state["message"],
        "model_available": os.path.exists(training_state["model_path"])
    }

# 📂 下载模型 (GET /model)
@router.get("/model")
def download_model():
    model_path = training_state["model_path"]
    if not os.path.exists(model_path):
        raise HTTPException(status_code=404, detail="模型文件未找到，请先训练")

    # 提供文件下载
    return FileResponse(
        path=model_path,
        filename="trained_model.zip",
        media_type='application/octet-stream'
    )