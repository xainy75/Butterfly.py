<div align="center">

# 🦋 Butterfly.py

**A mesmerizing butterfly curve rendered with Python's Turtle graphics**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)](LICENSE)
[![Turtle](https://img.shields.io/badge/Library-turtle-green?style=for-the-badge)](https://docs.python.org/3/library/turtle.html)

</div>

---

## ✨ Overview

**Butterfly.py** draws a stunning, colorful **butterfly curve** — a famous mathematical curve discovered by Temple H. Fay — using Python's built-in `turtle` graphics module. Each point on the curve is dynamically colored using trigonometric functions, producing a vibrant, rainbow-hued butterfly against a deep-purple night sky background.

---

## 🖼️ Preview

> The script renders a glowing, rainbow-colored butterfly curve on a dark `#1a0033` background — a beautiful blend of mathematics and art.

---

## 📐 The Mathematics

The butterfly curve is defined by the following **parametric equations**:

$$x(t) = \sin(t)\left(e^{\cos(t)} - 2\cos(4t) - \sin^5\!\left(\tfrac{t}{12}\right)\right)$$

$$y(t) = \cos(t)\left(e^{\cos(t)} - 2\cos(4t) - \sin^5\!\left(\tfrac{t}{12}\right)\right)$$

where `t` ranges from `0` to `2π` (approximately `6.283` radians).

Each plotted point is colored with RGB values derived from:

| Channel | Formula                    |
|---------|----------------------------|
| Red     | `abs(sin(2t))`             |
| Green   | `abs(cos(3t))`             |
| Blue    | `(1 + sin(5t)) / 2`        |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** — the `turtle` and `math` modules are included in the standard library; no additional packages are required.

### Installation

```bash
# Clone the repository
git clone https://github.com/xainy75/Butterfly.py.git

# Navigate into the project directory
cd Butterfly.py
```

### Running

```bash
python butterfly.py
```

A window will open and the butterfly curve will animate into view, dot by dot.

---

## 🗂️ Project Structure

```
Butterfly.py/
├── butterfly.py   # Main script — draws the butterfly curve
├── LICENSE        # Apache 2.0 License
└── README.md      # Project documentation
```

---

## 🛠️ How It Works

| Step | Description |
|------|-------------|
| 1    | Sets the canvas background to deep purple (`#1a0033`) |
| 2    | Iterates an integer `t` from `0` to `628` in steps of `2`; divides by `100` to get `t_rad` ∈ `[0, 6.26]` (≈ 2π radians) |
| 3    | Computes `(x, y)` coordinates from the parametric butterfly equations |
| 4    | Calculates a unique RGB color for each point using sine/cosine functions |
| 5    | Places a colored dot at the scaled position `(x × 85, y × 85)` |

---

## 📜 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ and mathematics

</div>
