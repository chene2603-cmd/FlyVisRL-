# FlyVisRL

Vision-based reinforcement learning for robust fruit fly locomotion in complex terrains using **FlyGym** and **PPO**.

## ✨ Features
- **Multi-terrain generalization**: Walks on gaps, blocks, and mixed terrains.
- **Biologically plausible vision**: Processes optic flow through T4a neuron responses.
- **Domain randomization**: Randomizes physics, terrain geometry, and visual noise.
- **Full data access**: Exposes neural activities, joint states, and contact forces via `info`.
- **Fixed implementation**: Neural activity correctly returned in `info['nn_activities']`.

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Train an agent (example)
python train.py

# Analyze gait & neural activity
python analyze.py
