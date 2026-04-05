# --- TASK 1: FILE I/O ---
print("--- Task 1: File Operations ---")

notes = [
    "Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes."
]

# Part A: Write and Append
with open("python_notes.txt", "w", encoding="utf-8") as f:
    for line in notes:
        f.write(line + "\n")
print("✓ python_notes.txt created successfully.")

with open("python_notes.txt", "a", encoding="utf-8") as f:
    # Adding two custom lines as requested
    f.write("Topic 6: File I/O allows data to be saved permanently.\n")
    f.write("Topic 7: APIs allow programs to talk to each other.\n")
print("✓ Lines appended successfully.")

# Part B: Read and Search
print("\nReading notes with line numbers:")
with open("python_notes.txt", "r", encoding="utf-8") as f:
    all_lines = f.readlines()
    for i, line in enumerate(all_lines, 1):
        print(f"{i}. {line.strip()}")

# Keyword Search
search_word = input("\nEnter a keyword to search in notes: ").strip().lower()
matches = [line.strip() for line in all_lines if search_word in line.lower()]

if matches:
    print(f"Found {len(matches)} match(es):")
    for m in matches: print(f"-> {m}")
else:
    print(f"No lines found containing '{search_word}'.")



import requests

def fetch_top_products():
    print("\n--- Task 2: Fetching 20 Products ---")
    url = "https://dummyjson.com/products?limit=20"
    
    try:
        # We add a 5-second timeout to prevent the script from hanging
        response = requests.get(url, timeout=5, verify=False)
        response.raise_for_status() # This triggers an error for 4xx or 5xx codes
        
        data = response.json()
        products = data['products']
        
        # Step 1: Formatted Table
        print(f"{'ID':<3} | {'Title':<25} | {'Price':<8} | {'Rating'}")
        print("-" * 55)
        for p in products:
            print(f"{p['id']:<3} | {p['title'][:25]:<25} | ${p['price']:<7} | {p['rating']}")
            
        # Step 2: Filter (Rating >= 4.5) and Sort (Price Descending)
        high_rated = [p for p in products if p['rating'] >= 4.5]
        high_rated.sort(key=lambda x: x['price'], reverse=True)
        
        print("\n--- High Rated Products (Rating >= 4.5, Sorted by Price) ---")
        for p in high_rated:
            print(f"- {p['title']} (${p['price']}) - Rating: {p['rating']}")

    except requests.exceptions.ConnectionError:
        print("Error: Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Try again later.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

fetch_top_products()


# Part A: Guarded Calculator
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print("\nTesting safe_divide:")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"ten / 2 = {safe_divide('ten', 2)}")

# Part B: Guarded File Reader
def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

print("\nTesting read_file_safe:")
read_file_safe("python_notes.txt") # Should work
read_file_safe("ghost_file.txt")   # Should fail gracefully



from datetime import datetime

def log_error(func_name, err_type, msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("error_log.txt", "a") as log:
        log.write(f"[{now}] ERROR in {func_name}: {err_type} — {msg}\n")

# --- Triggering Intentional Errors for Logger ---
print("\n--- Triggering Intentional Errors for Logger ---")

# 1. Connection Error Trigger (Using a fake URL)
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=2, verify=False)
except Exception as e:
    log_error("fetch_products", "ConnectionError", "Host unreachable")
    print("✓ Connection error logged.")

# 2. HTTP 404 Trigger (Handled safely with SSL bypass)
try:
    # Adding verify=False helps bypass the corporate SSL block
    res = requests.get("https://dummyjson.com/products/999", verify=False)
    if res.status_code != 200:
        log_error("lookup_product", "HTTPError", f"{res.status_code} Not Found for ID 999")
        print("✓ 404 error logged.")
except Exception as e:
    # If SSL still fails, we log it as an SSL error instead of crashing
    log_error("lookup_product", "SSLError", "Certificate verification failed")
    print("✓ SSL/Connection error logged.")

print("\nFinal Content of error_log.txt:")
with open("error_log.txt", "r") as f:
    print(f.read())

