import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from env.robust_env import RobustVisionFlyEnv

def run_training():
    os.makedirs("models", exist_ok=True)
    env = DummyVecEnv([lambda: RobustVisionFlyEnv(max_steps=5000)])
    model = PPO("MlpPolicy", env, n_steps=512)
    model.learn(50_000)
    model.save("models/ppo_fly_final.zip")