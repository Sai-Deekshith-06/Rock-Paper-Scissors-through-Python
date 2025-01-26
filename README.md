# Rock-Paper-Scissors-through-Python

## Overview

This Python project implements the classic **Rock-Paper-Scissors** game, where a player competes against the computer. The game includes text-to-speech feedback using the `pyttsx3` library for a more interactive experience.

## Features

- Randomized computer choices for fairness.
- Tracks scores for both the player and the computer.
- Announces the computer's choice and game results using text-to-speech.
- Provides error handling for invalid inputs.

## Requirements

- Python 3.x
- The `pyttsx3` library for text-to-speech functionality.

### Installing `pyttsx3`

To install the `pyttsx3` library, run the following command in your terminal or IDE:
```bash
pip install pyttsx3
```

## How to Play

1. Run the script:
   ```bash
   python rps.py
   ```
2. Enter your name when prompted.
3. Choose your move:
   - `1`: Rock
   - `2`: Paper
   - `3`: Scissors
   - `0`: End the game.
4. After each round:
   - The computer announces its choice.
   - The result of the round is displayed.
5. At the end of the game, the script announces the winner and final scores.

## Future Improvements

- Add graphical interface support (e.g., Tkinter or PyGame).
- Enhance text-to-speech with different voices and languages.