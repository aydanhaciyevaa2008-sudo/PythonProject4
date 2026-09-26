def check_length(password):
    return len(password) >= 12


def check_uppercase(password):
    return any(char.isupper() for char in password)


def check_lowercase(password):
    return any(char.islower() for char in password)


def check_digit(password):
    return any(char.isdigit() for char in password)


def check_special(password):
    return any(not char.isalnum() for char in password)


def calculate_score(password):
    score = 0

    if len(password) >= 8:
        score += 10

    if len(password) >= 12:
        score += 20

    if len(password) >= 16:
        score += 10

    if check_uppercase(password):
        score += 10

    if check_lowercase(password):
        score += 10

    if check_digit(password):
        score += 10

    if check_special(password):
        score += 15

    return score


def get_strength(score):
    if score < 30:
        return "Very Weak"
    elif score < 50:
        return "Weak"
    elif score < 70:
        return "Moderate"
    elif score < 85:
        return "Strong"
    else:
        return "Very Strong"