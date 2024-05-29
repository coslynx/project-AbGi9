import random
import string

def generate_random_username():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))

def generate_random_email():
    letters = string.ascii_lowercase
    domain = ['gmail.com', 'yahoo.com', 'outlook.com']
    username = ''.join(random.choice(letters) for i in range(8))
    email_domain = random.choice(domain)
    return f"{username}@{email_domain}"