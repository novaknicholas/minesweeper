# Console Minesweeper

A terminal-based Minesweeper implementation with a custom-generated board, cursor-based movement, and win/loss animations.

## Features
- Randomized board generation for any width/height (up to 60x60) with adjacent-mine-count calculation
- Recursive flood-fill reveal for connected empty (zero-adjacent) tiles
- Cursor-based movement (`w`/`a`/`s`/`d`) instead of coordinate input, with reveal/flag actions
- Win detection based on correct flag placement across the full board

## Run
```bash
python minesweeper.py
```

## Stack
Python (standard library only)
