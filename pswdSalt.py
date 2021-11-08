import hashlib
import os

pswd = "cs166SJSU"

pswd = hashlib.sha256(pswd.encode())

print(pswd)

print(pswd.hexdigest())

##### User input below ##### 

userPswd = input("Enter your password: ")
print(userPswd)

userPswdHash = hashlib.sha256(userPswd.encode())

print(userPswdHash.hexdigest())

##### Adding salt to hash #####

salt = os.urandom(32)

output = hashlib.pbkdf2_hmac('sha256', userPswd.encode(), salt, 100000, dklen=128)

print(output)

##### I'll add more to make it more complex #####

