# 🪰 FlyVisRL  
### *Vision-Powered Reinforcement Learning for Robust Fruit Fly Locomotion*

[![Made with FlyGym](https://img.shields.io/badge/Made%20with-FlyGym-3498db?logo=python&logoColor=white)](https://github.com/Neuroengineering-Lab/FlyGym)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)]()

> **Can a fruit fly learn to walk on alien terrains using only its eyes?**  
> In **FlyVisRL**, we train a biologically inspired agent that sees like a fly, thinks like a policy, and walks like it owns the ground — even when the world is full of gaps, blocks, and chaos.

---

## 🌟 Why It’s Cool

- 🧠 **Realistic Vision**: Processes optic flow through simulated **T4a neurons** — just like real flies!
- 🌍 **Multi-Terrain Mastery**: Trains on **gaps**, **blocks**, and **mixed landscapes** with domain randomization.
- ⚡ **Robust by Design**: Physics, terrain, and visual noise are randomized → no overfitting!
- 🔬 **Full Observability**: Access neural activity, joint torques, contact forces — perfect for analysis.
- ✅ **Fixed & Ready**: Neural data is correctly exposed in `info['nn_activities']` (no more missing signals!).

---

## 🚀 Quick Start

```bash
# 1. Clone & install
git clone https://github.com/yourname/FlyVisRL.git
cd FlyVisRL
pip install -r requirements.txt

# 2. Train your fly
python train.py

# 3. Watch it walk (coming soon: render + analysis)
python analyze.py
# 🪰 FlyVisRL  
### *Vision-Powered Reinforcement Learning for Robust Fruit Fly Locomotion*

[![Made with FlyGym](https://img.shields.io/badge/Made%20with-FlyGym-3498db?logo=python&logoColor=white)](https://github.com/Neuroengineering-Lab/FlyGym)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)]()

> **Can a fruit fly learn to walk on alien terrains using only its eyes?**  
> In **FlyVisRL**, we train a biologically inspired agent that sees like a fly, thinks like a policy, and walks like it owns the ground — even when the world is full of gaps, blocks, and chaos.

---

## 🌟 Why It’s Cool

- 🧠 **Realistic Vision**: Processes optic flow through simulated **T4a neurons** — just like real flies!
- 🌍 **Multi-Terrain Mastery**: Trains on **gaps**, **blocks**, and **mixed landscapes** with domain randomization.
- ⚡ **Robust by Design**: Physics, terrain, and visual noise are randomized → no overfitting!
- 🔬 **Full Observability**: Access neural activity, joint torques, contact forces — perfect for analysis.
- ✅ **Fixed & Ready**: Neural data is correctly exposed in `info['nn_activities']` (no more missing signals!).

---

## 🚀 Quick Start

```bash
# 1. Clone & install
git clone https://github.com/yourname/FlyVisRL.git
cd FlyVisRL
pip install -r requirements.txt

# 2. Train your fly
python train.py

# 3. Watch it walk (coming soon: render + analysis)
python analyze.py
💡 First run may take a minute to initialize the FlyGym backend.
FlyVisRL/
├── env/
│   └── robust_env.py      # Gym environment with vision + multi-terrain
├── train.py               # PPO training pipeline (Stable-Baselines3)
├── analyze.py             # Gait plots, neural heatmaps, terrain stats
├── models/                # 🚫 Ignored by Git — your trained agents live here
├── logs/                  # TensorBoard logs & monitoring
├── requirements.txt       # All dependencies
├── .gitignore             # Keeps virtual envs & caches out
└── LICENSE                # MIT — use, share, build upon!
📊 What You’ll Get

After training, your agent can:

Cross 2cm-wide gaps without falling 🕳️

Climb random block fields like a pro 🧱

Maintain balance under visual noise & physics perturbations 🌀

Output neural activity traces for scientific analysis 📈

(Example results coming soon!)

 

🤝 Contribute or Extend

This project is built for:

🧪 Neuroscience researchers studying sensorimotor control

🤖 RL engineers exploring embodied vision

🎓 Students learning biologically inspired AI

Want to add new terrains, different neurons (T5, LC), or imitation learning?
→ Fork it. Train it. Share it.

 

📜 License

MIT © [Your Name] — Free to use, modify, and deploy.
Just keep the credit, and go make something amazing.
📊 What You’ll Get

After training, your agent can:

Cross 2cm-wide gaps without falling 🕳️

Climb random block fields like a pro 🧱

Maintain balance under visual noise & physics perturbations 🌀

Output neural activity traces for scientific analysis 📈

(Example results coming soon!)

 

🤝 Contribute or Extend

This project is built for:

🧪 Neuroscience researchers studying sensorimotor control

🤖 RL engineers exploring embodied vision

🎓 Students learning biologically inspired AI

Want to add new terrains, different neurons (T5, LC), or imitation learning?
→ Fork it. Train it. Share it.

 

📜 License

MIT © [Your Name] — Free to use, modify, and deploy.
Just keep the credit, and go make something amazing.
📊 What You’ll Get

After training, your agent can:

Cross 2cm-wide gaps without falling 🕳️

Climb random block fields like a pro 🧱

Maintain balance under visual noise & physics perturbations 🌀

Output neural activity traces for scientific analysis 📈

(Example results coming soon!)

 

🤝 Contribute or Extend

This project is built for:

🧪 Neuroscience researchers studying sensorimotor control

🤖 RL engineers exploring embodied vision

🎓 Students learning biologically inspired AI

Want to add new terrains, different neurons (T5, LC), or imitation learning?
→ Fork it. Train it. Share it.

 

📜 License

MIT © [Your Name] — Free to use, modify, and deploy.
Just keep the credit, and go make something amazing.
"The fly doesn’t compute the world — it dances with it."
— Inspired by biological intelligence 🪰✨