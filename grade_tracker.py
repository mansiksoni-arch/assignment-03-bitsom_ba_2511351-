# --- TASK 1: CLEANING RAW STUDENT DATA ---
# Goal: Fix spacing, casing, and convert strings to numbers for 5 students.

for student in raw_students:
    # Removing extra spaces and fixing capitalization (e.g., 'ayesha' to 'Ayesha')
    clean_name = student["name"].strip().title()
    roll_int = int(student["roll"])
    
    # Converting the comma-separated string of marks into a list of integers
    marks_list = [int(m) for m in student["marks_str"].split(", ")]
    
    # VALIDATION: Checking if the name contains only letters
    # This 'if' statement decides which icon to print next to the name
    if clean_name.replace(" ", "").isalpha():
        validation_icon = "✓ Valid name"
    else:
        validation_icon = "✗ Invalid name"
    
    # Printing the formatted profile card
    print(f"{validation_icon}\n================================...")



# --- TASK 2: MARKS ANALYSIS & USER INTERACTION ---
# Part A: Assigning grades based on scores

for i in range(len(subjects)):
    score = marks[i]
    # This if-elif chain checks the score range to assign a letter grade
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
    print(f"{subjects[i]}: {score} ({grade})")

# Part B: Adding new subjects via user input
while True:
    sub_input = input("Enter subject: ").strip()
    # Using 'if' to check if the user wants to stop the loop
    if sub_input.lower() == "done":
        break
    
    # Validating that marks are numbers and within 0-100
    marks_input = input("Enter marks: ")
    if marks_input.isdigit():
        val = int(marks_input)
        if 0 <= val <= 100:
            # Add to list only if data is valid
            marks.append(val)



# --- TASK 3: CLASS SUMMARY REPORT ---
# Creating a table to show who passed based on their average score.

for name, scores in class_data:
    avg = sum(scores) / len(scores)
    
    # LOGIC: Pass if average is 60 or above, otherwise Fail
    if avg >= 60:
        status = "Pass"
    else:
        status = "Fail"
    
    # Formatting the table row
    print(f"{name:<18} | {avg:>7.2f} | {status}")



# --- TASK 4: STRING MANIPULATION ---
# Numbering sentences and ensuring proper punctuation.

for index, sentence in enumerate(sentences, 1):
    s = sentence.strip()
    # Adding a period ONLY if the sentence doesn't already have one
    if not s.endswith("."):
        s += "."
    print(f"{index}. {s}")



