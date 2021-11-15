import bcrypt

passwd = b's$cret12'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)

print(salt)
print(hashed)
