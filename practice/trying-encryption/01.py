import hashlib, binascii

# crypt = hashlib.sha256()
# crypt.update(b"hi")
# print(crypt.hexdigest())


dk = hashlib.pbkdf2_hmac('sha256', b'yo sup', b'qqqwqw', 10000000)
print(binascii.hexlify(dk))