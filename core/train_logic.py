import os
import torch
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.monitor import Monitor
from env.robust_env import RobustVisionFlyEnv

def make_env(seed=42):
    def _init():
        env = RobustVisionFlyEnv(
            terrain_types=['gap', 'blocks', 'mixed'],
            randomize_physics=True,
            add_visual_noise=True,
            max_steps=5000,  # 缩短测试时间
            seed=seed
        )
        return Monitor(env)
    return _init

def run_training(total_timesteps=50_000, model_save_path="models/ppo_fly_final.zip"):
    """被 backend 调用的训练函数"""
    os.makedirs("models", exist_ok=True)
    torch.manual_seed(42)
    
    env = DummyVecEnv([make_env(42)])
    model = PPO("MlpPolicy", env, verbose=0, n_steps=512, batch_size=64)
    model.learn(total_timesteps=total_timesteps)
    model.save(model_save_path)
    
    return {"status": "success", "model_path": model_save_path}