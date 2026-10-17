"""Inventory Manager project for CPS 310. Author: Jayden Spraggins."""

import os

INVENTORY_FILE = "inventory.txt"
LOW_STOCK_LIMIT = 5


def display_menu():
    """Display the main menu options for the inventory manager."""
    print("\nInventory Manager")
    print("1. View inventory")
    print("2. Add an item")
    print("3. Update an item quantity")
    print("4. Remove an item")
    print("5. Search inventory")
    print("6. View inventory summary")
    print("7. Exit")


def convert_quantity(text):
    """Return the text as a whole number, or None if it is not valid."""
    if not text.isdigit():
        return None
    try:
        return int(text)
    except ValueError:
        return None


def get_item_number(inventory, prompt):
    """Ask for an item number and return its list index, or None if invalid."""
    selection = input(prompt).strip()

    if not selection.isdigit():
        print("Invalid item number.")
        return None

    item_number = int(selection)
    if item_number < 1 or item_number > len(inventory):
        print("Invalid item number.")
        return None

    return item_number - 1


def load_inventory(filename):
    """Load inventory items from a pipe-delimited file into a list of dictionaries."""
    inventory = []

    # A missing file is fine. The program just starts with an empty list.
    if not os.path.exists(filename):
        return inventory

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            parts = line.split("|")
            if len(parts) != 3:
                continue

            name = parts[0].strip()
            category = parts[1].strip()
            quantity = convert_quantity(parts[2].strip())

            if name == "" or category == "" or quantity is None:
                continue

            item = {"name": name, "category": category, "quantity": quantity}
            inventory.append(item)

    return inventory


def save_inventory(inventory, filename):
    """Save the complete inventory list to the pipe-delimited file."""
    with open(filename, "w", encoding="utf-8") as file:
        for item in inventory:
            file.write(item["name"] + "|" + item["category"] + "|" + str(item["quantity"]) + "\n")


def view_inventory(inventory):
    """Display all inventory items in a numbered list."""
    if len(inventory) == 0:
        print("No inventory items found.")
        return

    print("Inventory:")
    number = 1
    for item in inventory:
        print(f"{number}. {item['name']} | {item['category']} | Quantity: {item['quantity']}")
        number += 1


def add_item(inventory):
    """Prompt for a new item, validate the input, and save it."""
    name = input("Enter the item name: ").strip()
    if name == "":
        print("Item name cannot be empty.")
        return
    if "|" in name:
        print("Item name cannot contain '|'.")
        return

    for item in inventory:
        if item["name"].lower() == name.lower():
            print("Item already exists.")
            return

    category = input("Enter the category: ").strip()
    if category == "":
        print("Category cannot be empty.")
        return
    if "|" in category:
        print("Category cannot contain '|'.")
        return

    quantity = convert_quantity(input("Enter the quantity: ").strip())
    if quantity is None:
        print("Quantity must be a nonnegative whole number.")
        return

    new_item = {"name": name, "category": category, "quantity": quantity}
    inventory.append(new_item)
    save_inventory(inventory, INVENTORY_FILE)
    print("Item added successfully.")


def update_quantity(inventory):
    """Update the quantity of a selected inventory item."""
    if len(inventory) == 0:
        print("No inventory items found.")
        return

    view_inventory(inventory)
    index = get_item_number(inventory, "Enter the item number to update: ")
    if index is None:
        return

    new_quantity = convert_quantity(input("Enter the new quantity: ").strip())
    if new_quantity is None:
        print("Quantity must be a nonnegative whole number.")
        return

    inventory[index]["quantity"] = new_quantity
    save_inventory(inventory, INVENTORY_FILE)
    print(f"{inventory[index]['name']} quantity updated to {new_quantity}.")


def remove_item(inventory):
    """Remove a selected inventory item and save the updated list."""
    if len(inventory) == 0:
        print("No inventory items found.")
        return

    view_inventory(inventory)
    index = get_item_number(inventory, "Enter the item number to remove: ")
    if index is None:
        return

    removed_item = inventory.pop(index)
    save_inventory(inventory, INVENTORY_FILE)
    print(f"Item removed: {removed_item['name']}")


def search_inventory(inventory):
    """Search inventory items by name using a case-insensitive partial match."""
    search_term = input("Enter part or all of an item name: ").strip()
    if search_term == "":
        print("Search term cannot be empty.")
        return

    matches = []
    for item in inventory:
        if search_term.lower() in item["name"].lower():
            matches.append(item)

    if len(matches) == 0:
        print("No inventory items matched your search.")
        return

    print("Matching items:")
    number = 1
    for item in matches:
        print(f"{number}. {item['name']} | {item['category']} | Quantity: {item['quantity']}")
        number += 1


def display_summary(inventory):
    """Display the summary statistics for all inventory items."""
    total_quantity = 0
    low_stock_count = 0
    category_counts = {}   # lowercase category -> number of items
    category_labels = {}   # lowercase category -> category as first typed

    for item in inventory:
        total_quantity += item["quantity"]

        if item["quantity"] < LOW_STOCK_LIMIT:
            low_stock_count += 1

        key = item["category"].strip().lower()
        if key in category_counts:
            category_counts[key] += 1
        else:
            category_counts[key] = 1
            category_labels[key] = item["category"].strip()

    print("Inventory Summary")
    print(f"Unique items: {len(inventory)}")
    print(f"Total quantity: {total_quantity}")
    print(f"Low-stock items: {low_stock_count}")

    print("\nItems by category:")
    if len(category_counts) == 0:
        print("No categories available.")
        return

    for key in sorted(category_counts):
        print(f"{category_labels[key]}: {category_counts[key]}")


def main():
    """Run the inventory manager menu until the user exits."""
    inventory = load_inventory(INVENTORY_FILE)

    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            update_quantity(inventory)
        elif choice == "4":
            remove_item(inventory)
        elif choice == "5":
            search_inventory(inventory)
        elif choice == "6":
            display_summary(inventory)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
