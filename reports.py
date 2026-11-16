from collections import defaultdict
from time_utils import minutes_to_time
from allocation import allocate_platforms


def platform_chart(trains, reserved_platforms, save_callback):
    print("\n================ PLATFORM CHART ================")
    if not trains:
        print("No trains available.")
        return

    assignments, total, _reserved_count = allocate_platforms(trains, reserved_platforms)
    if assignments is None:
        print("Unable to generate platform chart.")
        return

    for train in trains:
        train["platform"] = assignments[train["id"]]
    save_callback()

    ordered = sorted(trains, key=lambda item: (item["arrival"], item["departure"], item["id"]))
    print(f"\n{'ARRIVAL':<12}{'DEPARTURE':<12}{'TRAIN ID':<14}"
          f"{'TRAIN NAME':<20}{'CATEGORY':<18}{'PLATFORM':<12}")
    print("-" * 88)

    for train in ordered:
        print(f"{minutes_to_time(train['arrival']):<12}"
              f"{minutes_to_time(train['departure']):<12}"
              f"{train['id']:<14}{train['name'][:19]:<20}"
              f"{train['category']:<18}{assignments[train['id']]:<12}")

    print("\nMinimum platforms needed:", total)


def configure_reserved_platforms(current_reserved, save_callback):
    print("\n========== RESERVED PLATFORM SETTINGS ==========")
    print("Current reserved platform setting:", current_reserved)
    try:
        count = int(input("Enter number of reserved platforms: "))
        if count < 0:
            print("Number cannot be negative.")
            return current_reserved

        save_callback(count)
        print("Reserved platform setting updated.")
        print("The effective reserved count is automatically adjusted "
              "to preserve enough general platforms.")
        return count
    except ValueError:
        print("Enter a valid whole number.")
        return current_reserved


def platform_utilisation(trains, reserved_platforms):
    print("\n========== PLATFORM UTILISATION REPORT ==========")
    if not trains:
        print("No train records available.")
        return

    assignments, total, reserved_count = allocate_platforms(trains, reserved_platforms)
    if assignments is None or total == 0:
        print("Unable to calculate utilisation.")
        return

    start_time = min(train["arrival"] for train in trains)
    end_time = max(train["departure"] for train in trains)
    operating_time = end_time - start_time
    if operating_time <= 0:
        print("Invalid operating time.")
        return

    busy_time = defaultdict(int)
    train_count = defaultdict(int)
    for train in trains:
        platform = assignments[train["id"]]
        busy_time[platform] += train["departure"] - train["arrival"]
        train_count[platform] += 1

    all_platforms = (
        [f"R{i}" for i in range(1, reserved_count + 1)]
        + [f"P{i}" for i in range(1, total - reserved_count + 1)]
    )

    print(f"\nOperating period: {operating_time} minutes")
    print(f"Total platforms: {total}")
    print("\nPlatform-wise utilisation:")
    for platform in all_platforms:
        busy = busy_time[platform]
        percentage = (busy / operating_time) * 100
        print(f"\nPlatform {platform}"
              f"\nTrains handled: {train_count[platform]}"
              f"\nBusy time: {busy} minutes"
              f"\nUtilisation: {percentage:.2f}%")

    total_busy = sum(busy_time.values())
    overall = (total_busy / (total * operating_time)) * 100
    print("\nOverall Platform Utilisation:", f"{overall:.2f}%")
