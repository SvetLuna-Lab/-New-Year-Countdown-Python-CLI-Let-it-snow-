# cli.py

import argparse
from datetime import date

from countdown_basic import days_until_new_year
import countdown_snow

def main() -> None:
    parser = argparse.ArgumentParser(
        description="New Year countdown with optional ASCII snow animation."
    )
    parser.add_argument(
        "--mode",
        choices=["basic", "snow"],
        default="basic",
        help="Display mode: basic text or snow animation.",
    )
    args = parser.parse_args()

    if args.mode == "basic":
        days = days_until_new_year()
        print(f"Days left until New Year: {days}")
    elif args.mode == "snow":
        countdown_snow.main()

if __name__ == "__main__":
    main()
