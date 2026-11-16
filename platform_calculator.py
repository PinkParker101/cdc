def calculate_peak(trains, category=None):
    """Return the maximum number of trains present at one time."""
    events = []

    for train in trains:
        if category and train["category"] != category:
            continue
        events.append((train["arrival"], 1))
        events.append((train["departure"], -1))

    # At an identical time, a departure frees its platform before an arrival.
    events.sort(key=lambda event: (event[0], event[1]))

    current = 0
    maximum = 0
    for _time, change in events:
        current += change
        maximum = max(maximum, current)

    return maximum


def calculate_platforms(trains):
    print("\n========== PLATFORM REQUIREMENT ==========")
    if not trains:
        print("Register trains first.")
        return 0

    total = calculate_peak(trains)
    print(f"\nTotal trains registered: {len(trains)}")
    print(f"Minimum platforms required: {total}")
    return total
