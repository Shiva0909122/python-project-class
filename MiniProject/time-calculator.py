def get_valid_input(prompt, min_val, max_val):
    """Function to get valid integer input within a range"""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculate_end_time(hour, mins, dura):
    """Function to compute end time after adding duration"""
    total_minutes = hour * 60 + mins + dura
    end_hour = (total_minutes // 60) % 24  # Ensures it wraps in 24-hour format
    end_minute = total_minutes % 60
    
    # Convert to 12-hour AM/PM format
    am_pm = "AM" if end_hour < 12 else "PM"
    display_hour = end_hour if 1 <= end_hour <= 12 else (12 if end_hour == 0 or end_hour == 12 else end_hour % 12)

    return end_hour, end_minute, display_hour, am_pm

def main():
    """Main function to run the program"""
    while True:
        print("\n===== Time Calculator =====")
        hour = get_valid_input("Enter starting time (hours 0-23): ", 0, 23)
        mins = get_valid_input("Enter starting time (minutes 0-59): ", 0, 59)
        dura = get_valid_input("Enter event duration (minutes): ", 1, 10000)

        # Compute the end time
        end_hour, end_minute, display_hour, am_pm = calculate_end_time(hour, mins, dura)

        # Display results
        print(f"\nEnd time (24-hour format): {end_hour:02}:{end_minute:02}")
        print(f"End time (12-hour format): {display_hour:02}:{end_minute:02} {am_pm}")

        # Ask if the user wants another calculation
        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the Time Calculator! Goodbye.")
            break

# Run the program
if __name__ == "__main__":
    main()
