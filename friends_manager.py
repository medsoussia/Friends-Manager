import json

# ============================
# Functions
# ============================

def load_friends(filename="friends.json"):
    """Load friends from a JSON file."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_friends(friends, filename="friends.json"):
    """Save friends to a JSON file."""
    with open(filename, "w") as f:
        json.dump(friends, f, indent=4)

def add_friend(friends):
    """Add a friend to the list with input validation."""
    while True:
        name = input("\nEnter friend's name: ").strip()
        if name and name.replace(" ", "").isalpha():
            break
        else:
            print("Name must not be empty and contain only letters.")
    while True:
        try:
            age = int(input("Enter friend's age: ").strip())
            if age > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    while True:
        hobby = input("Enter friend's hobby: ").strip()
        if hobby and hobby.replace(" ", "").isalpha():
            break
        else:
            print("Hobby must not be empty and contain only letters.")
    friends.append({"name": name, "age": age, "hobby": hobby})
    print(f"{name} added successfully!")
    save_friends(friends)

def display_friends(friends):
    """Display all friends in the list."""
    if not friends:
        print("No friends in the list yet.")
        return
    print("\nList of friends:")
    for i, friend in enumerate(friends, start=1):
        print(f"{i} - Name: {friend['name']}, Age: {friend['age']}, Hobby: {friend['hobby']}")

def find_friend(friends, search_name):
    """Search for a friend by name (partial match, case-insensitive)."""
    results = [f for f in friends if search_name.lower() in f['name'].lower()]
    if results:
        print("\nSearch results:")
        for i, friend in enumerate(results, start=1):
            print(f"{i} - Name: {friend['name']}, Age: {friend['age']}, Hobby: {friend['hobby']}")
    else:
        print(f"No friends found matching '{search_name}'.")

def find_friend_index(friends, name):
    """Find exact friend index by name."""
    for i, f in enumerate(friends):
        if f['name'].lower() == name.lower():
            return i
    return -1

def delete_friend(friends):
    """Delete a friend by exact name."""
    if not friends:
        print("No friends to delete.")
        return
    name_to_delete = input("\nEnter the exact name of friend to delete: ").strip()
    index = find_friend_index(friends, name_to_delete)
    if index != -1:
        del friends[index]
        print(f"{name_to_delete} was deleted successfully!")
        save_friends(friends)
    else:
        print(f"{name_to_delete} not found on the list.")

# ============================
# Main Program
# ============================

def main():
    friends = load_friends()
    
    while True:
        print("\n=== FRIENDS MANAGER ===")
        print("1 - Add a friend")
        print("2 - Display all friends")
        print("3 - Search for a friend")
        print("4 - Delete a friend")
        print("5 - Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_friend(friends)
        elif choice == "2":
            display_friends(friends)
        elif choice == "3":
            search_name = input("Enter name to search: ").strip()
            find_friend(friends, search_name)
        elif choice == "4":
            delete_friend(friends)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
