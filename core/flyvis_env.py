import gym
from gym import spaces
import numpy as np

class FlyvisEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super().__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(10,), dtype=np.float32)

    def reset(self):
        return np.random.randn(10).astype(np.float32)

    def step(self, action):
        obs = np.random.randn(10).astype(np.float32)
        reward = float(np.random.rand())
        done = False
        info = {}
        return obs, reward, done, info

    def render(self, mode='human'):
        pass