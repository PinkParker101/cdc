from datetime import datetime


def time_to_minutes(time_value):
    """Accept either HH:MM text or minutes since midnight."""
    if isinstance(time_value, (int, float)):
        return int(time_value)

    try:
        parsed = datetime.strptime(str(time_value).strip(), "%H:%M")
        return parsed.hour * 60 + parsed.minute
    except ValueError:
        raise ValueError("Invalid time! Enter time in HH:MM format.")


def minutes_to_time(minutes):
    """Convert minutes since midnight into HH:MM."""
    minutes = int(minutes)
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def get_time(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return time_to_minutes(value)
        except ValueError as error:
            print(error)
