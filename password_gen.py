import random
import string
import argparse

def generate_password(length=12, use_digits=True, use_special_chars=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def check_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    strength = 0
    if len(password) >= 12:
        strength += 1
    if has_upper and has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    
    return strength

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Secure Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length")
    parser.add_argument("-d", "--no-digits", action="store_false", help="Exclude digits")
    parser.add_argument("-s", "--no-special", action="store_false", help="Exclude special chars")
    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_digits=args.no_digits,
        use_special_chars=args.no_special
    )
    strength = check_strength(password)
    
    print(f"🔒 Generated Password: {password}")
    print(f"⚡ Strength: {'★' * strength} ({strength}/4)")

