# ==========================================
# CP-049 PlatformPro
# Interval Scheduling Platform Allocation Engine
# ==========================================

trains = []


def time_to_minutes(time_str):
    try:
        h, m = map(int, time_str.split(":"))
        return h * 60 + m
    except:
        return None


def add_train():
    print("\n----- ADD TRAIN -----")

    train_id = input("Train ID: ").strip()

    for train in trains:
        if train["id"] == train_id:
            print("Train ID already exists!")
            return

    train_name = input("Train Name: ").strip()
    arrival = input("Arrival Time (HH:MM): ").strip()
    departure = input("Departure Time (HH:MM): ").strip()

    arr = time_to_minutes(arrival)
    dep = time_to_minutes(departure)

    if arr is None or dep is None:
        print("Invalid time format!")
        return

    if arr >= dep:
        print("Departure must be after arrival!")
        return

    trains.append({
        "id": train_id,
        "name": train_name,
        "arrival": arrival,
        "departure": departure,
        "platform": None
    })

    print("Train added successfully!")


def view_trains():
    print("\n----- TRAIN LIST -----")

    if len(trains) == 0:
        print("No trains added.")
        return

    for train in trains:
        print(
            f"ID: {train['id']} | "
            f"Name: {train['name']} | "
            f"Arrival: {train['arrival']} | "
            f"Departure: {train['departure']} | "
            f"Platform: {train['platform']}"
        )


def calculate_min_platforms():

    if len(trains) == 0:
        print("No trains available.")
        return

    arrivals = []
    departures = []

    for train in trains:
        arrivals.append(time_to_minutes(train["arrival"]))
        departures.append(time_to_minutes(train["departure"]))

    arrivals.sort()
    departures.sort()

    i = 0
    j = 0

    current = 0
    maximum = 0

    while i < len(arrivals) and j < len(departures):

        if arrivals[i] < departures[j]:
            current += 1
            maximum = max(maximum, current)
            i += 1
        else:
            current -= 1
            j += 1

    print(f"\nMinimum Platforms Required = {maximum}")


def assign_platforms():

    if len(trains) == 0:
        print("No trains available.")
        return

    sorted_trains = sorted(
        trains,
        key=lambda x: time_to_minutes(x["arrival"])
    )

    platform_end_time = {}

    for train in sorted_trains:

        arrival = time_to_minutes(train["arrival"])
        departure = time_to_minutes(train["departure"])

        assigned = False

        for platform_no in sorted(platform_end_time.keys()):

            if arrival >= platform_end_time[platform_no]:
                train["platform"] = platform_no
                platform_end_time[platform_no] = departure
                assigned = True
                break

        if not assigned:
            new_platform = len(platform_end_time) + 1
            train["platform"] = new_platform
            platform_end_time[new_platform] = departure

    print("Platform assignment completed!")


def handle_delay():

    if len(trains) == 0:
        print("No trains available.")
        return

    train_id = input("Enter Train ID: ")

    target = None

    for train in trains:
        if train["id"] == train_id:
            target = train
            break

    if target is None:
        print("Train not found!")
        return

    new_departure = input(
        "Enter New Departure Time (HH:MM): "
    )

    dep = time_to_minutes(new_departure)

    if dep is None:
        print("Invalid time!")
        return

    arr = time_to_minutes(target["arrival"])

    if dep <= arr:
        print("Departure must be after arrival.")
        return

    target["departure"] = new_departure

    assign_platforms()

    print("Delay updated successfully.")


def display_platform_chart():

    if len(trains) == 0:
        print("No trains available.")
        return

    print("\n=========== PLATFORM CHART ===========")

    sorted_trains = sorted(
        trains,
        key=lambda x: time_to_minutes(x["arrival"])
    )

    print("-" * 75)

    print(
        f"{'Train ID':<12}"
        f"{'Train Name':<20}"
        f"{'Arrival':<12}"
        f"{'Departure':<12}"
        f"{'Platform'}"
    )

    print("-" * 75)

    for train in sorted_trains:

        print(
            f"{train['id']:<12}"
            f"{train['name']:<20}"
            f"{train['arrival']:<12}"
            f"{train['departure']:<12}"
            f"{train['platform']}"
        )


def menu():

    while True:

        print("\n")
        print("====================================")
        print("       PLATFORMPRO - CP049")
        print("====================================")
        print("1. Add Train")
        print("2. View Trains")
        print("3. Calculate Minimum Platforms")
        print("4. Assign Platforms")
        print("5. Handle Train Delay")
        print("6. Display Platform Chart")
        print("7. Exit")

        choice = input("\nEnter Choice: ").strip()

        if choice == "1":
            add_train()

        elif choice == "2":
            view_trains()
            calculate_min_platforms()

        elif choice == "4":
            assign_platforms()

        elif choice == "5":
            handle_delay()

        elif choice == "6":
            display_platform_chart()

        elif choice == "7":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice!")


menu()
