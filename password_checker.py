import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "Add at least one uppercase letter.\n"

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "Add at least one lowercase letter.\n"

    # Digit check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks += "Include at least one number.\n"

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "Include at least one special character.\n"

    # Strength result
    if strength == 5:
        return "Strong Password ✅"
    elif 3 <= strength < 5:
        return "Moderate Password ⚠️\n" + remarks
    else:
        return "Weak Password ❌\n" + remarks


# Run program
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result = check_password_strength(pwd)
    print("\nResult:")
    print(result)