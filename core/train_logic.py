import os
from stable_baselines3 import PPO
from core.flyvis_env import FlyvisEnv

def run_training(timesteps=10000, model_path="models/ppo_fly_final.zip"):
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    env = FlyvisEnv()
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=timesteps)
    model.save(model_path)
    print(f"模型已保存至：{model_path}")