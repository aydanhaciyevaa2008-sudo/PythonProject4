from analyzer import (
    check_length,
    check_uppercase,
    check_lowercase,
    check_digit,
    check_special,
    calculate_score,
    get_strength
)

password = input("Enter your password: ")

print("\nPassword Analysis")
print("-----------------")

print("Length >= 12:", check_length(password))
print("Uppercase:", check_uppercase(password))
print("Lowercase:", check_lowercase(password))
print("Digit:", check_digit(password))
print("Special character:", check_special(password))

score = calculate_score(password)
strength = get_strength(score)

print("\nSecurity Score:", score, "/ 85")
print("Strength:", strength)