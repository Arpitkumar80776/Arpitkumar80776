import random
import string

#Let's make a random strong password generator
def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters))
    return password