# Monty Hall Problem Simulator

This project contains a Python script that simulates the Monty Hall problem, a well-known probability puzzle.

## Problem Description

The Monty Hall problem is a counter-intuitive statistics puzzle:

* There are 3 doors, behind which are two goats and a car.
* You pick a door (call it door A). You’re hoping for the car of course.
* Monty Hall, the game show host, examines the other doors (B & C) and opens one with a goat. (If both doors have goats, he picks randomly.)

Here’s the game: Do you stick with door A (original choice) or switch to the unopened door? Does it matter?

Surprisingly, the odds aren't 50-50. If you switch doors you'll win 2/3 of the time!

## Script Description

The script `monty_hall_simulator.py` is a simple simulation of this game which can be run to verify this probability. It takes two parameters:

* `switch_doors`: A boolean to represent the strategy the player uses. If it's True, the player switches their choice when offered. If False, they stick to their initial choice.
* `num_trials`: The number of times to run the simulation. The default value is 10,000 to get a reasonable estimation of the probabilities.

After running the specified number of trials, it calculates and outputs the estimated probability of winning under both strategies.

## How to Run

You can run the script using Python 3 as follows:

```sh
python monty_hall_simulator.py
