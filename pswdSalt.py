import hashlib
import os
import random
import bcrypt

##### User input below ##### 

userPswd = input("Enter your password: ")
print("User's Password: ", userPswd + '\n')

userPswdHash = hashlib.sha256(userPswd.encode())

print("User Password Hash: ", userPswdHash.hexdigest() + '\n')

##### Different methods of adding salt to hash #####

# Method 1: Use Python's random library and generate a random choice of characters

print("Method 1 Below \n")

pswdLength = range(8, 32)

characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
list = []
flag = True

while flag:
	userPswdLength = int(input("How long do you want your password to be? (range: 8 <= length <= 32): "))		
	if userPswdLength in range(8, 33):
		flag = False	
	
for i in range(userPswdLength):
	list.append(random.choice(characters))

salt1 = ""

for i in list:
	salt1 = salt1 + i

print("\nSalt Output using random lib:", salt1 + '\n')

# Method 2: Use Python's os library

print("Method 2 Below \n")

salt2 = (os.urandom(32)) # can add base 62 code here later to make it more complex

output2 = hashlib.pbkdf2_hmac('sha256', userPswd.encode(), salt2, 100000, dklen=128)

print("Salt Output using os lib: ", output2, "\n")

# Method 3: Use Python's bcrypt library

print("Method 3 Below \n")

userPswdBcrypt = "b'" + userPswd + "'" # need to add b in front because it changes its type from string to bytes -> a seq of octets, which is needed for bcrypt.gensalt()

userPswdBcrypt = bytes(userPswdBcrypt, 'utf-8')

salt3 = bcrypt.gensalt()

hash3 = bcrypt.hashpw(userPswdBcrypt, salt3)

check = bcrypt.checkpw(userPswdBcrypt, hash3)

print("Generated Salt: ", salt3, "\n")
print("Hashed Password with Salt using bcrypt lib: ", hash3, "\n")
print("Check to see if the hashed password matches: ", check, "\n")
