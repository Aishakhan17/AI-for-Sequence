# Sequence-AI

This repository builds upon the original [heksadecimal/sequence](https://github.com/heksadecimal/sequence) project.  
All AI development and recent changes are by [Aishakhan17](https://github.com/Aishakhan17).

Sequence is an abstract strategy board-and-card game. This game extends it with custom AI agents that can play the game intelligently. The goal is to explore and implement various AI strategies such as Minimax, Monte Carlo Tree Search (MCTS) and a Minimax-MCTS hybrid. The stretch goal is to use Monte Carlo

Sequence is a multiplayer board-and-card game that blends elements of strategy, memory, and chance.

## Requirements

Create a virtual environment before installing any dependencies:

-   Create Virtual Environment

```bash
python3 -m venv env_name
```

-   Activate Virtual Environment
    On Ubuntu

```bash
source env_name/bin/activate
```

    On Windows

```bash
source env_name\Scripts\activate
```

Install all dependencies using:

````bash
pip install -r requirements.txt


## How to play

After following the above steps, you can first move to the src directory and then execute main.py to start the game

```bash
cd src/
python main.py
````

### Game Rules

-   Each card is pictured **twice** on the game board (except Jacks).
-   Players place chips on spaces that match the cards in their hands.
-   **Two-eyed Jacks** are wild (can place anywhere), **one-eyed Jacks** remove opponent chips.
-   **Goal**: Form sequences of five connected chips (horizontally, vertically, or diagonally).
-   **Free corners** can be used by any player as part of a sequence.

### Winning

-   The game ends when a player complete a sequence of five cards. Cheers!
