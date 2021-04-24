from user import User
import basehash
import csv

hash_pas = basehash.base36()


def register(path):
    """This function register user."""
    user_name, password = enter_user()
    password_hash = hash_pas.hash(password)
    member = User(user_name, password_hash)
    member.add_file(path)

def enter_user():
    """This function get user name and password """
    user_name = input("Enter your user name :")
    password = input("Enter your password :")

    return user_name, password


def check(path):
    check_info=1
    """this function check user and password"""
    user_name, password = enter_user()
    password = int(password)
    with open(path, 'r') as user_file:
        reader = csv.reader(user_file)
        for row in reader:
            if row !='':
                if user_name == row[0]:
                    unhash_pass = hash_pas.unhash(row[1])
                    if password == unhash_pass:
                        print("welcome")
                        return check_info , user_name , password
                    else:
                        print("your password is wrong.")
                        for i in range(2):
                            password=int(input("Enter your password again"))
                            if password==unhash_pass:
                                print("welcome")
                                break
                        else:
                            print("You can try 1 hour later.")
                            break

        else:
            print("user name doesn't exist")
            check_info=0
    return check_info , user_name , password
# register()
#check()
