# Arkanoid Game with Pygame

This repository contains a simple implementation of the classic game Arkanoid using Python's Pygame library.

## Game Description

In the game, the player controls a paddle at the bottom of the screen and must bounce a ball against a wall of bricks at the top. The aim is to destroy all bricks using the ball, without letting the ball pass the paddle and hit the bottom of the screen. If the player manages to destroy all bricks, they win the game. If the ball hits the bottom of the screen, the player loses.

## How to Play

- Use the left and right arrow keys to move the paddle.
- The ball will bounce off the paddle and the walls of the window.
- If the ball hits a brick, the brick disappears and the ball bounces back.
- The player loses if the ball goes below the paddle.
- The player wins if all bricks are destroyed.

## Requirements

To run the game, you need:
- Python 3.x
- Pygame

If you do not have Pygame installed, you can install it using pip:

```bash
pip install pygame

python arkanoid.py
