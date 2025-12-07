# Repository Guidelines

## Project Structure & Module Organization
Source lives in `game/`, split by responsibility: `main.py` orchestrates the pygame loop, `player.py` handles movement and HP, `level.py` defines obstacles, `questions.py` stores Q&A data, and `config.py` centralizes constants and asset paths. `assets/` holds art, photos, and audio placeholders (create `assets/sounds/` before committing new tracks). Packaging metadata and the console entry point sit in `setup.py`, while editable docs live at the repo root.

## Build, Test, and Development Commands
Bootstrap inside a virtualenv and install the package in editable mode:
```bash
python3 -m venv venv && source venv/bin/activate
pip install -e .
```
Run the game either through the console script or the module:
```bash
game            # preferred, uses entry point
python -m game.main
```
When iterating on assets, keep pygame caches clean by restarting the process after changing image or sound files.

## Coding Style & Naming Conventions
Follow PEP 8 with 4-space indentation, snake_case for functions/modules, and PascalCase for classes. Keep constants in `config.py` scream case (e.g., `SCREEN_WIDTH`). Favor small, focused modules and reuse helper methods inside `Player` and `Level` rather than duplicating pygame math. Document non-obvious logic with short inline comments; longer explanations belong in docstrings.

## Testing Guidelines
Automated tests are not yet in place; prioritize manual playtesting after each gameplay change by running `game` and exercising the menu, movement, and question prompts. When adding tests, use `pytest`, nest files under `tests/`, and name modules `test_<feature>.py`. Aim for coverage of question validation, HP adjustments, and collision helpers. Mock pygame surfaces where needed to keep tests headless.

## Commit & Pull Request Guidelines
Commits follow Conventional Commits (`feat(game): …`, `docs(README.md): …`). Keep messages in the imperative present tense and scope changes narrowly. Pull requests should describe gameplay impact, list manual test steps (e.g., “launched `game`, answered prompt”), and attach screenshots or short clips whenever UI elements change. Link related issues and call out asset additions so reviewers can verify licensing before merge.

## Assets & Configuration Tips
Reference new media via relative paths inside `game/config.py` so builds remain portable. Store large binaries in `assets/` and avoid embedding absolute paths in code. If you introduce custom sounds, ensure the mixer initializes by shipping silent placeholders, mirroring the current background music treatment.
