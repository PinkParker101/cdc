from time_utils import get_time, minutes_to_time
from storage import save_data


def get_train(trains, train_id):
    for train in trains:
        if train["id"] == train_id:
            return train
    return None


def register_train(trains, reserved_platforms):
    print("\n========== REGISTER TRAIN ==========")
    train_id = input("Enter Train ID: ").strip()

    if not train_id:
        print("Train ID cannot be empty.")
        return

    if get_train(trains, train_id):
        print("Train ID already exists!")
        return

    name = input("Enter Train Name: ").strip()
    if not name:
        print("Train name cannot be empty.")
        return

    arrival = get_time("Enter Arrival Time (HH:MM): ")
    departure = get_time("Enter Departure Time (HH:MM): ")

    if departure <= arrival:
        print("Departure must be later than arrival.")
        return

    print("\nTrain Category:")
    print("1. Local")
    print("2. Long Distance")
    category_choice = input("Choose category: ").strip()

    if category_choice == "1":
        category = "Local"
    elif category_choice == "2":
        category = "Long Distance"
    else:
        print("Invalid category!")
        return

    trains.append({
        "id": train_id,
        "name": name,
        "arrival": arrival,
        "departure": departure,
        "category": category
    })
    save_data(trains, reserved_platforms)
    print("\nTrain registered successfully!")


def view_trains(trains):
    print("\n================ REGISTERED TRAINS ================")
    if not trains:
        print("No trains registered yet.")
        return

    print(f"{'ID':<12}{'TRAIN NAME':<20}{'ARRIVAL':<12}"
          f"{'DEPARTURE':<12}{'CATEGORY':<18}")
    print("-" * 74)

    for train in sorted(trains, key=lambda item: (item["arrival"], item["id"])):
        print(f"{train['id']:<12}{train['name'][:19]:<20}"
              f"{minutes_to_time(train['arrival']):<12}"
              f"{minutes_to_time(train['departure']):<12}"
              f"{train['category']:<18}")
