from storage import load_data, save_data
from train_manager import register_train, view_trains
from platform_calculator import calculate_platforms
from allocation import assign_platforms
from delay_manager import handle_delay
from reports import platform_chart, configure_reserved_platforms, platform_utilisation


def main():
    trains, reserved_platforms = load_data()

    def save_current_data():
        save_data(trains, reserved_platforms)

    while True:
        print("\n")
        print("=" * 55)
        print("             PLATFORMPRO SYSTEM")
        print("      Interval-Scheduling Platform Allocation")
        print("=" * 55)
        print("1. Register Train")
        print("2. View Registered Trains")
        print("3. Calculate Minimum Platforms")
        print("4. Assign Platforms")
        print("5. Handle Train Delay")
        print("6. Display Platform Chart")
        print("7. Configure Reserved Platforms")
        print("8. Platform Utilisation Report")
        print("9. Exit")
        print("=" * 55)

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            register_train(trains, reserved_platforms)
        elif choice == "2":
            view_trains(trains)
        elif choice == "3":
            calculate_platforms(trains)
        elif choice == "4":
            assign_platforms(trains, reserved_platforms, save_current_data)
        elif choice == "5":
            handle_delay(trains, reserved_platforms, save_current_data)
        elif choice == "6":
            platform_chart(trains, reserved_platforms, save_current_data)
        elif choice == "7":
            def save_new_reserved(value):
                nonlocal reserved_platforms
                reserved_platforms = value
                save_data(trains, reserved_platforms)
            reserved_platforms = configure_reserved_platforms(
                reserved_platforms, save_new_reserved
            )
        elif choice == "8":
            platform_utilisation(trains, reserved_platforms)
        elif choice == "9":
            save_current_data()
            print("\nThank you for using PlatformPro!")
            print("Train records saved successfully.")
            break
        else:
            print("Invalid choice! Please select 1-9.")


if __name__ == "__main__":
    main()
