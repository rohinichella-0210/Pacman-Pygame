# Pacman-Pygame
A classic Pac-Man clone built in Python using Pygame.

---

## Overview
This project recreates the core Pac-Man gameplay loop: maze navigation, dot collection, animated Pac-Man, randomly moving ghosts, collision detection, and a restartable game-over screen — all rendered with simple Pygame shapes, no external sprites required.

## Tech Stack

| Layer | Technology |
|---|---|
| Core logic | Python |
| Rendering & Input | Pygame |
| Graphics | Custom-drawn shapes |
| Maze data | 2D list grid |

## Module Breakdown

| Component | Responsibility |
|---|---|
| `grid` | Maze layout — walls, paths, dots |
| `pacman` | Position, direction, and mouth animation |
| `ghosts` | Ghost positions and colors |
| `move_pacman()` | Movement and dot-eating logic |
| `move_ghost()` | Randomized ghost movement |
| `draw_pacman()` / `draw_ghost()` | Rendering |
| `reset_game()` | Resets maze and score |
| `draw_game_over()` | Game-over screen |

## Game Flow
```
Player Input
     |
     v
Pac-Man Movement & Dot Collection
     |
     v
Ghost Movement
     |
     v
Collision Check
     |
     v
Render Frame
     ^
     |
Game Over -> Restart (SPACE)
```

## Highlights
- Grid-based movement with timed updates
- Animated Pac-Man mouth that follows direction
- Four ghosts with random wall-aware movement
- Live scoring and collision-based game over
- Instant restart without relaunching
- No external assets - fully drawn with Pygame

## Controls
```
Arrow Keys -> Move
SPACE      -> Restart after Game Over
```

## Setup

**1. Install dependency**
```
pip install pygame
```

**2. Run**
```
python pacman.py
```

## Roadmap
- Power pellets and frightened-mode ghosts
- Smarter ghost pathfinding
- Multiple levels
- Sound effects
- High-score saving

## License
For academic / learning purposes only
