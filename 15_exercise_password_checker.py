# input username and password.
# print a statement: "{username}, your password {*******} is {n} letters long"
# where n is length of password

username = input('enter username: ')
password = input('enter password: ')
password_length = len(password)
secret = '*'*password_length
print(f"{username}, your password {secret} is {password_length} letters long")
