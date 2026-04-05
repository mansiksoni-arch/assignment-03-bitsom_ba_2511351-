import copy

# --- PROVIDED DATA ---
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


# List of categories to group by
categories = ["Starters", "Mains", "Desserts"]

print("--- Task 1: Explore the Menu ---")

for cat in categories:
    print(f"===== {cat} =====")
    for item, info in menu.items():
        # Check if this item belongs to the current category
        if info["category"] == cat:
            status = "Available" if info["available"] else "Unavailable"
            # :<15 creates padding so the columns line up
            print(f"{item:<15} ₹{info['price']:>6.2f}   [{status}]")
    print() # Adds a blank line between categories



cart = []

def add_to_cart(item_name, qty):
    # 1. Check if the item is even in the menu
    if item_name not in menu:
        print(f"Error: {item_name} is not on the menu.")
        return

    # 2. Check if it's available
    if not menu[item_name]["available"]:
        print(f"Error: {item_name} is currently unavailable.")
        return

    # 3. Search if it's ALREADY in the cart
    found = False
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += qty
            found = True
            break
    
    # 4. If it wasn't found, add it as a new entry
    if not found:
        new_entry = {
            "item": item_name, 
            "quantity": qty, 
            "price": menu[item_name]["price"]
        }
        cart.append(new_entry)
    
    print(f"Added {qty} x {item_name} to cart.")

# Now you can simulate the steps:
add_to_cart("Paneer Tikka", 2)
add_to_cart("Gulab Jamun", 1)
add_to_cart("Paneer Tikka", 1) # This will trigger the 'found = True' logic



# Task 2: Cart Operations
cart = []

# --- FUNCTION: ADD TO CART ---
def add_to_cart(item_name, qty):
    # 1. Check if item exists in menu
    if item_name not in menu:
        print(f"Error: '{item_name}' is not on the menu.")
        return

    # 2. Check if item is available
    if not menu[item_name]["available"]:
        print(f"Error: '{item_name}' is currently unavailable.")
        return

    # 3. Check if it's already in the cart to update quantity
    found = False
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += qty
            found = True
            break
    
    # 4. If not found, add as a new entry
    if not found:
        cart.append({"item": item_name, "quantity": qty, "price": menu[item_name]["price"]})
    print(f"Action: Added {qty} x {item_name}")

# --- FUNCTION: REMOVE FROM CART ---
def remove_from_cart(item_name):
    for entry in cart:
        if entry["item"] == item_name:
            cart.remove(entry)
            print(f"Action: Removed {item_name} from cart.")
            return
    print(f"Error: {item_name} not found in cart.")

# --- FUNCTION: UPDATE QUANTITY ---
def update_cart(item_name, new_qty):
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] = new_qty
            print(f"Action: Updated {item_name} quantity to {new_qty}.")
            return
    print(f"Error: {item_name} not found in cart.")



print("\n--- Simulating Order Sequence ---")
add_to_cart("Paneer Tikka", 2)
add_to_cart("Gulab Jamun", 1)
add_to_cart("Paneer Tikka", 1)  # Should update quantity to 3
add_to_cart("Mystery Burger", 1) # Should show error
add_to_cart("Chicken Wings", 1)  # Should show error (unavailable)
remove_from_cart("Gulab Jamun")

# Print cart state to verify
print("\nCurrent Cart State:", cart)



print("\n" + "="*36)
print("          ORDER SUMMARY          ")
print("="*36)

subtotal = 0
for entry in cart:
    item_total = entry["quantity"] * entry["price"]
    subtotal += item_total
    print(f"{entry['item']:<18} x{entry['quantity']}   ₹{item_total:>7.2f}")

gst = subtotal * 0.05
total_payable = subtotal + gst

print("-" * 36)
print(f"{'Subtotal:':<24} ₹{subtotal:>7.2f}")
print(f"{'GST (5%):':<24} ₹{gst:>7.2f}")
print(f"{'Total Payable:':<24} ₹{total_payable:>7.2f}")
print("="*36)



# --- TASK 3: INVENTORY TRACKER ---
print("\n--- Task 3: Inventory Management ---")

# Creating an independent clone of the inventory
inventory_backup = copy.deepcopy(inventory)

# PROOF: Manually change one value in the original
inventory["Paneer Tikka"]["stock"] = 999
print(f"Original Stock (Paneer Tikka): {inventory['Paneer Tikka']['stock']}")
print(f"Backup Stock (Paneer Tikka)  : {inventory_backup['Paneer Tikka']['stock']}")

# Restore original state before continuing
inventory["Paneer Tikka"]["stock"] = 10
print("✓ Inventory restored for simulation.")



print("\nUpdating Inventory based on Order...")

for entry in cart:
    item_name = entry["item"]
    qty_ordered = entry["quantity"]
    
    if item_name in inventory:
        current_stock = inventory[item_name]["stock"]
        
        # Check if we have enough stock
        if current_stock >= qty_ordered:
            inventory[item_name]["stock"] -= qty_ordered
        else:
            print(f"⚠ Warning: Insufficient stock for {item_name}. Deducting remaining {current_stock}.")
            inventory[item_name]["stock"] = 0



print("\n--- Inventory Alerts ---")
for item, data in inventory.items():
    stock = data["stock"]
    level = data["reorder_level"]
    
    # If stock is at or below reorder level, trigger alert
    if stock <= level:
        print(f"⚠ Reorder Alert: {item} — Only {stock} unit(s) left (reorder level: {level})")

# Final verification of the Deep Copy
print(f"\nFinal Check: Original 'Paneer Tikka' stock is {inventory['Paneer Tikka']['stock']}, "
      f"while Backup remains {inventory_backup['Paneer Tikka']['stock']}.")



# --- TASK 4: DAILY SALES LOG ANALYSIS ---
print("\n" + "="*40)
print("--- Task 4: Daily Sales Log Analysis ---")

# Part A: Revenue Calculation
daily_revenue = {}
best_day = ""
max_revenue = -1

for date, orders in sales_log.items():
    day_total = sum(order["total"] for order in orders)
    daily_revenue[date] = day_total
    
    # Check for Best-Selling Day
    if day_total > max_revenue:
        max_revenue = day_total
        best_day = date

# Print Daily Revenue Table
print(f"{'Date':<12} | {'Revenue':>10}")
print("-" * 25)
for date, rev in daily_revenue.items():
    print(f"{date:<12} | ₹{rev:>9.2f}")

print(f"\n🏆 Best-Selling Day: {best_day} (₹{max_revenue:.2f})")


# Part B: Most Ordered Item
item_frequency = {}

for orders in sales_log.values():
    for order in orders:
        # We use set(items) if we only care about unique orders, 
        # but here we count every appearance in an order
        for dish in order["items"]:
            item_frequency[dish] = item_frequency.get(dish, 0) + 1

# Finding the Max value in the frequency dictionary
most_ordered = max(item_frequency, key=item_frequency.get)
print(f"🔥 Most Ordered Item: {most_ordered} ({item_frequency[most_ordered]} times)")



# Part C: Add New Day & Numbered List
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\n--- Complete Order History (All Dates) ---")
all_orders = []

# Flatten the nested dictionary into a simple list for easy numbering
for date, orders in sales_log.items():
    for order in orders:
        all_orders.append({"date": date, "order": order})

# Using enumerate starting from 1
for i, entry in enumerate(all_orders, 1):
    d = entry["date"]
    o = entry["order"]
    items_str = ", ".join(o["items"])
    print(f"{i}. [{d}] Order #{o['order_id']} — ₹{o['total']:.2f} — Items: {items_str}")














