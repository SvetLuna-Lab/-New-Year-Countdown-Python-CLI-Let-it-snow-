# countdown_snow.py

import os
import random
import time
from datetime import date

WIDTH = 40
HEIGHT = 12
SNOWFLAKES_PER_FRAME = 3
FRAME_DELAY = 0.2  # seconds


def days_until_new_year() -> int:
    today = date.today()
    new_year = date(today.year + 1, 1, 1)
    return (new_year - today).days


def clear_screen() -> None:
    # Cross-platform screen clear
    os.system("cls" if os.name == "nt" else "clear")


def draw_frame(snow_positions: list[tuple[int, int]], days: int) -> None:
    # Create empty screen buffer
    screen = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Draw snowflakes
    for x, y in snow_positions:
        if 0 <= y < HEIGHT and 0 <= x < WIDTH:
            screen[y][x] = "*"

    # Draw info line with days until New Year at the bottom
    info = f" Days left until New Year: {days} "
    info = info[:WIDTH] if len(info) > WIDTH else info
    info_start = max(0, (WIDTH - len(info)) // 2)
    info_y = HEIGHT - 1
    for i, ch in enumerate(info):
        screen[info_y][info_start + i] = ch

    clear_screen()
    for row in screen:
        print("".join(row))


def update_snow(snow_positions: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # Move existing snowflakes down
    new_positions: list[tuple[int, int]] = []
    for x, y in snow_positions:
        new_y = y + 1
        if new_y < HEIGHT:
            new_positions.append((x, new_y))

    # Add new snowflakes at the top
    for _ in range(SNOWFLAKES_PER_FRAME):
        x = random.randint(0, WIDTH - 1)
        new_positions.append((x, 0))

    return new_positions


def main() -> None:
    days = days_until_new_year()
    snow: list[tuple[int, int]] = []

    try:
        # Simple animation loop: several seconds
        for _ in range(80):
            snow = update_snow(snow)
            draw_frame(snow, days)
            time.sleep(FRAME_DELAY)
    except KeyboardInterrupt:
        clear_screen()
        print(f"Days left until New Year: {days}")


if __name__ == "__main__":
    main()
