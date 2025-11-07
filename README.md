# New Year Countdown – Python CLI (Let it snow)

This project is a Python-based reimagining of a “Let it snow” task:
it shows how many days are left until New Year and can display a small
ASCII-art snow animation in the terminal.

The project demonstrates different levels of implementation:

- **basic** – simple function that calculates days until New Year and prints the result;
- **snow** – ASCII animation of falling snowflakes in the terminal with the countdown displayed;
- **CLI** – a small command-line interface that lets you choose between modes.

---

## Structure

```text
countdown_basic.py   # simple days-until-New-Year calculation
countdown_snow.py    # ASCII snow animation + countdown in the terminal
cli.py               # command-line entry point (basic/snow modes)
README.md


Usage

Basic mode
python cli.py --mode basic


Output example:

Days left until New Year: 42


Snow mode (ASCII animation)

python cli.py --mode snow

This will show a simple falling-snow animation in the terminal with the number
of days left until New Year displayed at the bottom.

Press Ctrl+C to stop the animation.


Requirements

Python 3.10+ (or compatible)

No external dependencies – only the Python standard library is used.


Ideas for further extension

Add localization (English/Russian text).

Add an option to change the duration of the animation or frame size.

Package this as a pip-installable CLI tool.



## How to run

Basic mode:

```bash
python cli.py --mode basic
Snow animation mode:

bash

python cli.py --mode snow
