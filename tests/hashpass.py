import hashlib
import os

users = {} # A simple demo storage

# Add a user
username = 'Brent' # The users username
password = 'mypassword' # The users password

salt = os.urandom(32) # A new salt for this user
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = { # Store the salt and key
    'salt': salt,
    'key': key
}

# Verification attempt 1 (incorrect password)
username = 'Brent'
password = 'notmypassword'

salt = users[username]['salt'] # Get the salt
key = users[username]['key'] # Get the correct key
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key != new_key # The keys are not the same thus the passwords were not the same

# Verification attempt 2 (correct password)
username = 'Brent'
password = 'mypassword'

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key == new_key # The keys are the same thus the passwords were the same

# Adding a different user
username = 'Jarrod'
password = 'my$ecur3p@$$w0rd'

salt = os.urandom(32) # A new salt for this user
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = {
    'salt': salt,
    'key': key
}

# Checking the other users password
username = 'Jarrod'
password = 'my$ecur3p@$$w0rd'

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key == new_key # The keys are the same thus the passwords were the same for this user also