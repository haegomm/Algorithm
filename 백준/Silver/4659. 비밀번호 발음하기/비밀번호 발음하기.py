while True:
    password = input().strip()

    if password == 'end':
        break

    vowels = "aeiou"
    has_vowel = False
    valid = True

    for i in range(len(password)):
        current_char = password[i]

        if current_char in vowels:
            has_vowel = True

        if i < len(password) - 2:
            if (current_char in vowels and
                    password[i + 1] in vowels and
                    password[i + 2] in vowels) or \
               (current_char not in vowels and
                    password[i + 1] not in vowels and
                    password[i + 2] not in vowels):
                valid = False
                break

        if i < len(password) - 1:
            if current_char == password[i + 1] and current_char not in "eo":
                valid = False
                break

    if valid and has_vowel:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")