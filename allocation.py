from platform_calculator import calculate_peak


def allocate_platforms(trains, reserved_platforms):
    """Allocate platforms while keeping local trains off reserved platforms."""
    if not trains:
        return {}, 0, 0

    total = calculate_peak(trains)
    if total == 0:
        return {}, 0, 0

    local_peak = calculate_peak(trains, "Local")
    long_peak = calculate_peak(trains, "Long Distance")

    reserved_count = min(
        reserved_platforms,
        long_peak,
        total - local_peak
    )
    general_count = total - reserved_count

    reserved = [f"R{i}" for i in range(1, reserved_count + 1)]
    general = [f"P{i}" for i in range(1, general_count + 1)]

    available = {platform: 0 for platform in reserved + general}
    assignments = {}

    ordered_trains = sorted(
        trains,
        key=lambda train: (
            train["arrival"],
            0 if train["category"] == "Long Distance" else 1,
            train["departure"],
            train["id"]
        )
    )

    for train in ordered_trains:
        arrival = train["arrival"]
        free_reserved = [p for p in reserved if available[p] <= arrival]
        free_general = [p for p in general if available[p] <= arrival]

        platform = None
        if train["category"] == "Long Distance":
            if free_reserved:
                platform = free_reserved[0]
            elif free_general:
                platform = free_general[0]
        elif free_general:
            platform = free_general[0]

        if platform is None:
            return None, total, reserved_count

        assignments[train["id"]] = platform
        available[platform] = train["departure"]

    return assignments, total, reserved_count


def assign_platforms(trains, reserved_platforms, save_callback):
    print("\n========== PLATFORM ALLOCATION ==========")
    if not trains:
        print("Register trains first.")
        return

    assignments, total, reserved_count = allocate_platforms(trains, reserved_platforms)
    if assignments is None:
        print("Allocation failed. Check platform restrictions.")
        return

    for train in trains:
        train["platform"] = assignments[train["id"]]

    save_callback()
    print(f"\nMinimum platforms used: {total}")
    print(f"Reserved platforms used: {reserved_count}")
    print(f"General platforms used: {total - reserved_count}")
    print("\nPlatform allocation completed successfully!")

    for train in sorted(trains, key=lambda item: item["arrival"]):
        print(f"Train {train['id']} ({train['name']}) -> Platform {assignments[train['id']]}")
