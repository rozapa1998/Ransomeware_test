import string
import random

char_lenght = int(input("Please, enter the leght of the password: "))

#import string to use all special and normal characters.
char = string.ascii_letters + string.digits + string.punctuation

#Use join to use variable char to generate password randomly, aditionaly use char_lenght to set range to the iteration
password = "".join(random.choice(char) for i in range(char_lenght))

print("Your safe password is:" + password)


