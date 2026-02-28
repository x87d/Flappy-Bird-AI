# 🐦 Flappy Bird — NEFT AI (No ML Libraries)

A self-learning Flappy Bird AI built from scratch using **Neuro-Evolution with Fixed Topologies (NEFT)** and **Pygame**. No TensorFlow, no PyTorch — just pure Python and math.

![Preview](preview.gif)

---

## What is NEFT?

**NEFT (Neuro-Evolution with Fixed Topologies)** is a genetic algorithm that trains a neural network by evolving its connection weights across generations — without ever changing the network's structure. Think of it as natural selection for neural networks.

Each bird in the simulation has its own small brain (a 3-input → 1-output neural network). Birds that survive longer pass on their weights to the next generation, gradually producing birds that learn to navigate the pipes.

Unlike **NEAT**, which also evolves the network topology, NEFT keeps the architecture fixed and only mutates weights — making it simpler to implement and understand.

---

## How It Works

**Each bird sees 3 inputs:**
- Distance from its center to the top pipe's bottom edge
- Horizontal distance to the next pipe
- Distance from its center to the bottom pipe's top edge

**The output** is a single value — if it exceeds `0.73`, the bird flaps.

**Each generation:**
1. All birds play simultaneously until they all die
2. Fitness is calculated based on lifespan
3. Birds are grouped into species based on weight similarity
4. Champions are cloned; offspring are produced via mutation
5. Stale or extinct species are culled

---

## Project Structure

```
├── main.py          # Game loop, rendering, pipe spawning
├── config.py        # Window settings and shared state
├── components.py    # Ground and Pipes classes
├── player.py        # Bird logic, vision, decision-making
├── brain.py         # Neural network (feed-forward)
├── node.py          # Individual neuron with sigmoid activation
├── connection.py    # Weighted connection between nodes, with mutation
├── population.py    # Population management and natural selection
├── species.py       # Speciation, fitness tracking, offspring generation
└── requirements.txt
```

---

## Installation

**Requirements:** Python 3.7+

```bash
# 1. Clone the repository
git clone https://github.com/your-username/neft-flappy-bird.git
cd neft-flappy-bird

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the simulation
python main.py
```

---

## Controls

There are none — sit back and watch the AI learn. 🎉

The HUD displays the current **generation** and **obstacle count** in the bottom-left corner.

---

## Configuration

Key parameters you can tweak in the source files:

| Parameter | Location | Default | Effect |
|---|---|---|---|
| Population size | `main.py` | `100` | More birds = faster learning, more CPU |
| Pipe opening gap | `components.py` | `100` | Smaller = harder |
| Pipe spawn interval | `main.py` | `200` frames | Lower = more frequent pipes |
| Mutation rate | `brain.py` | `80%` | Probability a connection mutates |
| Speciation threshold | `species.py` | `1.2` | Lower = more species |
| Staleness limit | `population.py` | `8` generations | Before a species is culled |
| Flap threshold | `player.py` | `0.73` | Output value needed to trigger a flap |

---

## Dependencies

- [pygame](https://www.pygame.org/) `2.1.2` — rendering and game loop only. All AI logic is implemented from scratch.

---

## License

MIT — free to use, modify, and distribute.
