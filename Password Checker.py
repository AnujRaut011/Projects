import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Check for uppercase characters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # Check for lowercase characters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # check for digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    # Check for special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    # Strength evaluation
    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback


# Main Program
password = input("Enter your password: ")
strength, suggestions = check_password_strength(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("Suggestions to improve:")
    for tip in suggestions:
        print("-", tip)
