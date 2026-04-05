# Raw student data with inconsistent formatting
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]
print("--- Task 1: Data Parsing & Profile Cleaning ---")

# We create an empty list to store the cleaned data for later use
cleaned_students = []

for student in raw_students:
    # 1. Clean the name: Remove spaces and fix capitalization
    clean_name = student["name"].strip().title()
    
    # 2. Convert roll number from text to a whole number (integer)
    roll_int = int(student["roll"])
    
    # 3. Clean marks: Split the string into a list and convert each to an integer
    # This is called a 'List Comprehension' - it's a shortcut for a loop
    marks_list = [int(m) for m in student["marks_str"].split(", ")]
    
    # 4. Name Validation: Check if the name only contains alphabets
    # We remove spaces temporarily just for this check
    is_valid = clean_name.replace(" ", "").isalpha()
    validation_icon = "✓ Valid name" if is_valid else "✗ Invalid name"
    
    # Save this cleaned data into our new list
    cleaned_students.append({"name": clean_name, "roll": roll_int, "marks": marks_list})
    
    # 5. Print the Profile Card using f-strings
    print(f"{validation_icon}")
    print("================================")
    print(f"Student : {clean_name}")
    print(f"Roll No : {roll_int}")
    print(f"Marks   : {marks_list}")
    print("================================\n")
# After the loop, find student 103
for student in cleaned_students:
    if student["roll"] == 103:
        name_103 = student["name"]
        print(f"Special Case (Roll 103):")
        print(f"ALL CAPS: {name_103.upper()}")
        print(f"lowercase: {name_103.lower()}")

# Task 2 Data
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

print("\n--- Task 2: Marks Analysis ---")
print(f"Report for {student_name}:")

for i in range(len(subjects)):
    score = marks[i]
    
    # The Grading Logic
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
    
    print(f"{subjects[i]:<10}: {score} [Grade: {grade}]")

# Calculations
total_marks = sum(marks)
average_marks = total_marks / len(marks)

# Finding Highest and Lowest
# We use .index() to find which subject matches the top score
max_score = max(marks)
min_score = min(marks)
top_subject = subjects[marks.index(max_score)]
bottom_subject = subjects[marks.index(min_score)]

print(f"\nTotal Marks   : {total_marks}")
print(f"Average Marks : {average_marks:.2f}") # .2f rounds to 2 decimal places
print(f"Highest Score : {top_subject} ({max_score})")
print(f"Lowest Score  : {bottom_subject} ({min_score})")

print("\n--- Add New Subjects (Type 'done' to finish) ---")
new_count = 0

while True:
    sub_input = input("Enter subject name: ").strip()
    
    if sub_input.lower() == "done":
        break  # This stops the loop immediately
    
    marks_input = input(f"Enter marks for {sub_input}: ")
    
    # Validation: Check if the input is a number
    if marks_input.isdigit():
        score = int(marks_input)
        
        # Check if marks are in the valid range 0-100
        if 0 <= score <= 100:
            subjects.append(sub_input)
            marks.append(score)
            new_count += 1
            print(f"✓ Added {sub_input}")
        else:
            print("✗ Error: Marks must be between 0 and 100.")
    else:
        print("✗ Error: Please enter a valid number for marks.")

# Final Update
updated_avg = sum(marks) / len(marks)
print(f"\nNew subjects added: {new_count}")
print(f"Updated Class Average: {updated_avg:.2f}")

# Task 3 Data
class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]
print("\n" + "="*40)
print(f"{'Name':<18} | {'Average':>7} | {'Status'}")
print("-" * 40)

pass_count = 0
fail_count = 0
total_class_avg = 0
topper_name = ""
topper_avg = -1 # Start with a low number to compare

for name, scores in class_data:
    # Calculate average for this specific student
    avg = sum(scores) / len(scores)
    total_class_avg += avg # Add to class total for the final average
    
    # Determine Status
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1
        
    # Check for Topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name
        
    # Print the row with perfect alignment
    # :<18 means left-align in 18 spaces
    # :>7.2f means right-align in 7 spaces with 2 decimals
    print(f"{name:<18} | {avg:>7.2f} | {status}")

print("-" * 40)

class_final_avg = total_class_avg / len(class_data)

print(f"Passed: {pass_count} | Failed: {fail_count}")
print(f"Class Topper: {topper_name} ({topper_avg:.2f})")
print(f"Overall Class Average: {class_final_avg:.2f}")

print("\n" + "="*40)
print("--- Task 4: String Manipulation Utility ---")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# 1. Strip whitespace
clean_essay = essay.strip()
print(f"1. Clean Essay: {clean_essay}")

# 2. Title Case
print(f"2. Title Case: {clean_essay.title()}")

# 3. Count 'python' (case-insensitive)
# We use .lower() to make sure we find 'python' even if it was 'Python'
python_count = clean_essay.lower().count("python")
print(f"3. Count of 'python': {python_count}")

# 4. Replace 'python' with Emoji
replaced_essay = clean_essay.replace("python", "Python 🐍")
print(f"4. Replaced: {replaced_essay}")

# 5. Split into sentences
sentences = clean_essay.split(". ")
print(f"5. Sentences List: {sentences}")

# 6. Numbered sentences
print("\n6. Numbered Sentences:")
for index, sentence in enumerate(sentences, 1):
    # Strip any extra spaces from the sentence itself
    s = sentence.strip()
    # Add a period if it's missing (since .split removes them)
    if not s.endswith("."):
        s += "."
    print(f"{index}. {s}")

