from time_utils import get_time, minutes_to_time
from train_manager import get_train
from allocation import allocate_platforms


def handle_delay(trains, reserved_platforms, save_callback):
    print("\n========== TRAIN DELAY MANAGEMENT ==========")
    if not trains:
        print("No trains available.")
        return

    train_id = input("Enter Train ID: ").strip()
    train = get_train(trains, train_id)
    if not train:
        print("Train not found!")
        return

    print("\nCurrent Schedule:")
    print("Arrival:", minutes_to_time(train["arrival"]))
    print("Departure:", minutes_to_time(train["departure"]))
    print("Platform:", train.get("platform", "Not allocated"))

    print("\nEnter the updated schedule:")
    new_arrival = get_time("New Arrival Time (HH:MM): ")
    new_departure = get_time("New Departure Time (HH:MM): ")
    if new_departure <= new_arrival:
        print("Departure must be later than arrival.")
        return

    old_arrival, old_departure = train["arrival"], train["departure"]
    train["arrival"], train["departure"] = new_arrival, new_departure

    assignments, _total, _reserved_count = allocate_platforms(trains, reserved_platforms)
    if assignments is None:
        train["arrival"], train["departure"] = old_arrival, old_departure
        print("Updated schedule could not be allocated.")
        print("Original schedule has been restored.")
        return

    for item in trains:
        item["platform"] = assignments[item["id"]]

    save_callback()
    print("\nDelay updated successfully!")
    print("New arrival:", minutes_to_time(new_arrival))
    print("New departure:", minutes_to_time(new_departure))
    print("New platform:", assignments[train_id])
    print("\nAll train platforms have been reallocated.")
    print("\nUpdated Allocation:")
    for item in sorted(trains, key=lambda value: value["arrival"]):
        print(f"{item['id']} -> {assignments[item['id']]}")
