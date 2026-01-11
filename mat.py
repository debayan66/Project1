import re
# re module (regular) searches for patterns in a string
def check(password):
    strength_points = 0
    reasons = []

    # Length check
    if len(password) >= 8:
        strength_points += 1
        reasons.append("Length is 8 or more")
    else:
        reasons.append("Length is less than 8")

    # Uppercase
    if re.search(r"[A-Z]", password):
        strength_points += 1
        reasons.append("Contains uppercase letter")
    else:
        reasons.append("No uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        strength_points += 1
        reasons.append("Contains lowercase letter")
    else:
        reasons.append("No lowercase letter")

    # Numbers
    if re.search(r"[0-9]", password):
        strength_points += 1
        reasons.append("Contains number")
    else:
        reasons.append("No number")

    # Special chars
    if re.search(r"[@$!%*?&]", password):
        strength_points += 1
        reasons.append("Contains special character")
    else:
        reasons.append("No special character")

    # Final label
    if strength_points == 5:
        label = "STRONG"
    elif strength_points >= 3:
        label = "MEDIUM "
    else:
        label = "WEAK"

    return label, reasons


if __name__ == "__main__":
    pwd = input("Enter your password: ")
    strength, reasons = check(pwd)

    print("\nPassword Strength:", strength)
    print("\nDetails:")
    for i in reasons:
        print("-", i)
