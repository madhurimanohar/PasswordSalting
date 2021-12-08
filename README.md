# PasswordSalting

## Method 1 - Random

We are using Python's [random](https://docs.python.org/3/library/random.html) library to generate a random choice of characters for the user's password. This method is not ideal since it's easy to crack.

## Method 2 - OS

We are using Python's [os](https://docs.python.org/3/library/os.html) library and sha256 hash function to encode and salt the user's password. User can input their password which we will then encrypt and add salt to.

## Method 3 - Bcrypt

We are using Pythons [bcrypt](https://www.npmjs.com/package/bcrypt) library.

To use this import you need to install bcrypt first. Run the command:
```bash
sudo pip3 install bcrypt
```

`gensalt()` creates salt which we can add to the hashed password.

## Method 4 - Secrets

We are using Python's [secrets](https://docs.python.org/3/library/secrets.html) library. This library helps generate a cryptographically strong random numbers which can be used to generate passwords.

`secrets.token_hex()` accepts a postivie number that denotes the number of bytes in a hex format. The function returns a randomly generated hex string of the specified number of bytes.
