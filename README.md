# PasswordSalting

## Method 1

We are using Python's 'random' library to generate a random choice of characters for the user's password. This method is not ideal since it's easy to crack.

## Method 2

We are using Python's 'os' library and sha256 hash function to encode and salt the user's password. User can input their password which we will then encrypt and add salt to.

## Method 3

We are using Pythons 'bcrypt' library.

To use this import you need to install bcrypt first. Please run the command **sudo pip3 install bcrypt** on your terminal before importing.

gensalt() creates salt which we can add to the hashed password.
