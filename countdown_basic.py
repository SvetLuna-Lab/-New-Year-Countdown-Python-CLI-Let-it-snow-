# countdown_basic.py

from datetime import datetime, date

def days_until_new_year(today: date | None = None) -> int:
    if today is None:
        today = date.today()
    new_year = date(today.year + 1, 1, 1)
    diff = new_year - today
    return diff.days

def main() -> None:
    days = days_until_new_year()
    print(f"Days left until New Year: {days}")

if __name__ == "__main__":
    main()
