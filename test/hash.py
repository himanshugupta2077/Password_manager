import hashlib
import os

salt = os.urandom(100) 
# salt = b'salt'
passw = b'qwerty'
crypt = hashlib.pbkdf2_hmac('sha256', passw, salt, 1000000)
print(crypt.hex())

q = "qwerty"
q = q.encode('utf-8')
print(q)