from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from pantry import Pantry
from prettytable import PrettyTable

def main():
    print(f"Basic Pantry Tracker - IN PROGRESS📒")
    pantry_file_path = "pantry_items.csv"
    
    while True:
        print(f"\n✨ Welcome to your pantry, what would you like to do today? ✨")
        print(f"   1. 🛍️  Add Item")
        print(f"   2. ❌  Remove Item")
        print(f"   3. 🕵️  View Pantry")
        print(f"   4. 🛒  Quit Pantry")

        choice = int(input(f"Enter choice [1/2/3/4]: "))

        if choice == 1:
            # add item
            item = add_item()

            # store item
            store_item(item, pantry_file_path)

        elif choice == 2:
            # remove item
            remove_item(item, pantry_file_path)

        elif choice == 3:
            # view pantry
            view_pantry(pantry_file_path)
        
        elif choice == 4:
            break

        else:
            print(f"Invalid Choice.")

def add_item():
    print(f"🎯 Item added:")
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter item quantity: "))

    expiry_month = input("Enter expiry month (mm): ").zfill(2)
    expiry_year = input("Enter expiry year (yy): ").zfill(2)
    item_expiry_date = f"28-{expiry_month}-{expiry_year}"

    item_categories = [
        "🍎 Fruits",
        "🥕 Vegetables",
        "🌾 Grains",
        "🥛 Dairy",
        "🥩 Meat",
        "🍤 Seafood",
        "☕ Beverages",
        "🍫 Snacks",
        "🧂 Condiments",
        "🌶️  Spices",
        "🧁 Baking Supplies",
        "🍴 Other"
    ]

    while True:
        print(f"Select item category:")
        for i, category in enumerate(item_categories):
            print(f"  {i+1}. {category}")
        
        value_range = f"1 - {len(item_categories)}"
        selected_index = int(input(f"Enter category number {value_range}: ")) - 1

        if selected_index in range(len(item_categories)):
            item_category = item_categories[selected_index]
            new_item = Pantry(
                item_name=item_name, 
                quantity=item_quantity, 
                expiry_date=item_expiry_date, 
                category=item_category)
            return new_item
        else:
            print("Invalid category.")

def store_item(item: Pantry, pantry_file_path):
    print(f"🎯 Item stored: {item}")

    with open(pantry_file_path, "a", encoding="utf-8") as f:
        f.write(f"{item.item_name},{item.quantity},{item.category},{item.expiry_date}\n")

def remove_item(item: Pantry, pantry_file_path):
    print(f"🎯 Item removed: ") # pending

def view_pantry(pantry_file_path):
    print(f"🎯 Pantry:")

    pantry_items = []
    with open(pantry_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            item_name, item_quantity, item_category, item_expiry_date = line.strip().split(",")
            line_pantry = Pantry(
                item_name=item_name, 
                quantity=item_quantity, 
                category=item_category, 
                expiry_date=item_expiry_date)
            pantry_items.append(line_pantry)
    
    table = PrettyTable()
    table.field_names = ["Item Name", "Quantity", "Category", "Expiry Date"]

    today = date.today()
    warning_date = today + relativedelta(days=7)

    for item in pantry_items:
        expiry_date = datetime.strptime(item.expiry_date, "%d-%m-%y").date()
        table.add_row([item.item_name, item.quantity, item.category, item.expiry_date])
    
    print(table)

    for item in pantry_items:
        expiry_date = datetime.strptime(item.expiry_date, "%d-%m-%y").date()
        if expiry_date <= warning_date:
            days_remaining = (expiry_date - today).days
            if days_remaining > 0:
                print(red(f"⚠️  Warning: {item.item_name} expires on {item.expiry_date} (in {days_remaining} days)!"))
            else:
                print(red(f"⚠️  Warning: {item.item_name} expired!"))

def red(text):
    return f"\033[31m{text}\033[0m"

if __name__ == "__main__":
    main()