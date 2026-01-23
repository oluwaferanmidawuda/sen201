from skills import add_log, view_logs

def menu():
    while True:
        print("\n--- Soft Skill Progress Tracker ---")
        print("1. Add Skill Improvement Log")
        print("2. View Logs")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_log()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
