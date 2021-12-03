import secrets
import random

#CSPRNG for number of X number of bits
print("\n\nSecrets Package - Random Bits")
rand_bits = secrets.randbits(20)
print("Binary: ", bin(rand_bits))
print("Decimal: ", rand_bits)
rand_bits = secrets.randbits(20)
print("\nBinary: ", bin(rand_bits))
print("Decimal: ", rand_bits)

#Extra functions that offer different types of random number generation
print("\n\nEXTRA")
#Random package is not CSPRNG
systemRandom = random.SystemRandom()
print("\nRandom Package\nRandom Number from 1 - 50")
randomNumber = randomNumber = systemRandom.randint(1, 50)
print(randomNumber)
#Secrets Package (CSPRNG)
secretsGenerator = secrets.SystemRandom()
print("Secrets Package - Random Range")
rand_num2 = secretsGenerator.randrange(0, 1000, 100)
print(rand_num2)
print("Secrets Package - Random Int from 1 - 100")
rand_num = secretsGenerator.randint(0, 100)
print(rand_num)
print("Secrets Package - Random Choice from non empty list")
num_list = [1, 2, 3, 5, 7, 11, 13, 17]
choice = secretsGenerator.choice(num_list)
print(num_list)
print(choice)
print("Secrets Package - Random Sample from list")
sample = secretsGenerator.sample(num_list, 3)
print(sample)