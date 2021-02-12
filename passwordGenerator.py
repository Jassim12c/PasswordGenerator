import random
import string

# ask the user how long they want their password to be
# Have a mix of uppercase and lowercase letters as well as numbers and symbols
# The password should be a minimum of 6 characters long

_Password = None
T = True

upper_lower_case = list(string.ascii_letters)
random.shuffle(upper_lower_case)
digits = list(string.digits)
random.shuffle(digits)
punctuation = list(string.punctuation)
random.shuffle(punctuation)

while T:
    try:
        user = int(input("How long do you want your password to be? (has to be above 6) \n>.. "))
        while user < 6:
            user = int(input("***Oops, it has to be above 6*** \n>.. "))
    except ValueError as error:
        print("That's not a valid value")
        print("{}".format(error))
    else:
        blank = user * "*"
        _Password = blank
        T = False

T = True
print("")
print("***Now please put in how many letters, numbers and symbols you want. make sure it equals {}***".format(user))
print("")

while T:
    try:

        u_sub = user

        print("you have {} characters left".format(u_sub))

        letters = int(input("How many letters do you want? \n>.. "))

        if letters > u_sub or letters > len(upper_lower_case):
            print("\n* An error has occurred, Please start over again")
            print("* The number of letters can't be bigger than {} \n".format(len(upper_lower_case)))
            continue

        print("")

        u_sub = user - letters
        if u_sub == 0:
            numbers = 0
            symbols = 0
            break
        numbers = int(input("How many numbers do you want? ***you have {} characters left.*** \n>.. ".format(u_sub)))

        if numbers > u_sub or numbers > len(digits):
            print("\n* An error has occurred, Please start over again")
            print("* The number of digits can't be bigger than {} \n".format(len(digits)))
            continue

        u_sub -= numbers
        print("")

        if u_sub == 0:
            symbols = 0
            break
        symbols = int(input("How many symbols do you want? ie: '%$#@!*' ***you have {} characters left.*** \n>.. ".
                            format(u_sub)))

        if symbols > u_sub or symbols > len(punctuation):
            print("\n* An error has occurred, Please start over again")
            print("* The number of punctuations can't be bigger than {} \n".format(len(punctuation)))
            continue

    except ValueError as Error:
        print("That's not a valid value, Please start over again.")

    else:
        T = False

letters_random = random.sample(upper_lower_case, k=letters)
digits_random = random.sample(digits, k=numbers)
punctuation_random = random.sample(punctuation, k=symbols)

Empty_list = []
Empty_list.extend(letters_random)
Empty_list.extend(digits_random)
Empty_list.extend(punctuation_random)

random.shuffle(Empty_list)
P = "".join(Empty_list)

Password = _Password.replace("*" * user, P)
print(Password)

Password_no_repeat = [Password]
