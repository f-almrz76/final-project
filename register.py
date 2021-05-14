from user import User
import basehash
import csv
from colorama import Fore
import log
from admin import Admin
hash_pas = basehash.base36()


def register_user(user_name, password, path):
    """
    this function register user and save to file.
    :param user_name: user name of user.
    :param password: password of user.
    :param path: address of file.
    """
    password_hash = hash_pas.hash(password)
    member = User(user_name, password_hash)
    member.add_file(path)

def register_admin(admin_name,password,path):
    """
      this function register user and save to file.
      :param user_name: user name of user.
      :param password: password of user.
      :param path: address of file.
      """
    password_hash = hash_pas.hash(password)
    member = Admin(admin_name, password_hash)
    member.add_file(path)

def check_user(name, path):
    """
    This function check that user name doesn't exist.
    :param name: user name such that give from
    :param path: address of file for check name.
    :return:0 if user name exists and 1 if name doesn't exist.
    """
    try:
        with open(path, 'r') as users:
            user_read = csv.DictReader(users)
            for row in user_read:
                if row['user name'] == name:
                    return 0
            else:
                    return 1

    except:
        return 1


def enter_user():
    """This function get user name and password and return them. """
    user_name = input("Enter your user name :")
    password = input("Enter your password :")
    return user_name, password


def check(path):
    """
    This function controls user name and password exist and if they mach with input ,
    allow to enter.
    :param path: address of file such that user names save it.
    :return: check_info for checking user name and password enter correct and user name
    and password.
    """
    check_info = 1
    user_name, password = enter_user()
    password = int(password)
    with open(path, 'r') as user_file:
        reader = csv.DictReader(user_file)
        for row in reader:
            if user_name == row['user name']:
                unhash_pass = hash_pas.unhash(row['password'])
                if password == unhash_pass:
                    print(f"welcome {user_name}")
                    return check_info, user_name, password
                else:
                    print(Fore.RED + "your password is wrong.")
                    for i in range(2):
                        password = int(input("Enter your password again"))
                        if password == unhash_pass:
                            print(f"welcome {user_name}")
                            return check_info, user_name, password
                            break
                    else:
                        print(Fore.RED + "You can try 1 hour later.")
                        log.warning_logger.error(f"{user_name} enters 3 times wrong password")
                        check_info = 0
                        return check_info, user_name, password
                        break

        else:
            print(Fore.RED + "user name doesn't exist")
            check_info = 0
            return check_info, user_name, password


#d = enter_user()
"""
ch = check_user('fateme', 'admin.csv')
print(ch)
if ch or ch == None:
    print(ch)"""