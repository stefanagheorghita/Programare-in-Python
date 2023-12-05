import random
import string


def password_generator(length=8, special_chars=False, numbers=False, mixed_case=False):
    minimum = 0
    if special_chars:
        minimum += 1
    if numbers:
        minimum += 1
    if mixed_case:
        minimum += 2
    if length < minimum:
        return "Cannot generate password with given requirements"
    characters = string.ascii_letters if mixed_case else string.ascii_lowercase
    characters += string.digits if numbers else ''
    characters += string.punctuation if special_chars else ''
    password = ''.join(random.choice(characters) for i in range(length))
    count_lower = sum(1 for c in password if c.islower())
    count_upper = sum(1 for c in password if c.isupper())
    count_digits = sum(1 for c in password if c.isdigit())
    count_special = sum(1 for c in password if not c.isalnum())
    pos_lower = [i for i, c in enumerate(password) if c.islower()]
    pos_upper = [i for i, c in enumerate(password) if c.isupper()]
    pos_digits = [i for i, c in enumerate(password) if c.isdigit()]
    pos_special = [i for i, c in enumerate(password) if not c.isalnum()]
    posi = [pos_lower, pos_upper, pos_digits, pos_special]
    if numbers and count_digits == 0:
        disp = [i for i in range(length)]
        pos = random.choice(disp)
        disp.remove(pos)
        cat = -1
        for i in range(len(posi)):
            try:
                index = posi[i].index(pos)
            except ValueError:
                continue
            if index != -1:
                cat = i
                break
        while len(posi[cat]) == 1:
            pos = random.choice(disp)
            disp.remove(pos)
            for i in range(len(posi)):
                try:
                    index = posi[i].index(pos)
                except ValueError:
                    continue
                if index != -1:
                    cat = i
                    break
        password = password[:pos] + random.choice(string.digits) + password[pos + 1:]
        count_lower = sum(1 for c in password if c.islower())
        count_upper = sum(1 for c in password if c.isupper())
        count_digits = sum(1 for c in password if c.isdigit())
        count_special = sum(1 for c in password if not c.isalnum())
        pos_lower = [i for i, c in enumerate(password) if c.islower()]
        pos_upper = [i for i, c in enumerate(password) if c.isupper()]
        pos_digits = [i for i, c in enumerate(password) if c.isdigit()]
        pos_special = [i for i, c in enumerate(password) if not c.isalnum()]
        posi = [pos_lower, pos_upper, pos_digits, pos_special]
    if special_chars and count_special == 0:

        disp = [i for i in range(length)]
        pos = random.choice(disp)
        disp.remove(pos)
        cat = -1
        for i in range(len(posi)):
            try:
                index = posi[i].index(pos)
            except ValueError:
                continue
            if index != -1:
                cat = i
                break
        while len(posi[cat]) == 1:
            pos = random.choice(disp)
            disp.remove(pos)
            for i in range(len(posi)):
                try:
                    index = posi[i].index(pos)
                except ValueError:
                    continue
                if index != -1:
                    cat = i
                    break
        password = password[:pos] + random.choice(string.punctuation) + password[pos + 1:]
        count_lower = sum(1 for c in password if c.islower())
        count_upper = sum(1 for c in password if c.isupper())
        count_digits = sum(1 for c in password if c.isdigit())
        count_special = sum(1 for c in password if not c.isalnum())
        pos_lower = [i for i, c in enumerate(password) if c.islower()]
        pos_upper = [i for i, c in enumerate(password) if c.isupper()]
        pos_digits = [i for i, c in enumerate(password) if c.isdigit()]
        pos_special = [i for i, c in enumerate(password) if not c.isalnum()]
        posi = [pos_lower, pos_upper, pos_digits, pos_special]
    if mixed_case and (count_lower == 0 or count_upper == 0):
        disp = [i for i in range(length)]
        pos = random.choice(disp)
        disp.remove(pos)
        cat = -1
        for i in range(len(posi)):
            try:
                index = posi[i].index(pos)
            except ValueError:
                continue
            if index != -1:
                cat = i
                break
        while len(posi[cat]) == 1:
            pos = random.choice(disp)
            disp.remove(pos)
            for i in range(len(posi)):
                try:
                    index = posi[i].index(pos)
                except ValueError:
                    continue
                if index != -1:
                    cat = i
                    break
        if count_lower == 0:
            password = password[:pos] + random.choice(string.ascii_lowercase) + password[pos + 1:]
        else:
            password = password[:pos] + random.choice(string.ascii_uppercase) + password[pos + 1:]

    return password
