import random
import string

def generate_password(length):
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password
length = int(input("enter the length or your password:"))
password = generate_password(length)
print(f"your password is: {password}")
