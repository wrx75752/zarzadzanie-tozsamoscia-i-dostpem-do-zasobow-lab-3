import random
import string

def generate_secure_password():
    special_characters = "!@#$%^&*()_-+=<>?/[]{}|"

    password_length = random.randint(8, 32)
    password = []

    # Add characters characters
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(special_characters))

    # Fill the rest of the password with random characters
    for _ in range(password_length - len(password)):
        password.append(random.choice(string.ascii_letters + string.digits + special_characters))

    random.shuffle(password)

    # Return the password as a string
    return ''.join(password)

# Example usage
secure_password = generate_secure_password()
print(f"Secure password: {secure_password}")
