import csv
import basehash
import pandas as pd
from pathlib import Path
import json
import event
import log
from colorama import Fore
hash_pas = basehash.base36()


class User:

    def __init__(self, user_name, password):
        self.user_name=user_name
        self.password=password
        self.money = 0

    def buy(self, id, num, code):
        """
        this function is for buying tickets of the event.
        :param id: id of event that want to buy.
        :param num: number of ticket that want to buy.
        :param code: code if discount.
        """
        with open('Event.csv', 'r') as events:
            events_read = csv.DictReader(events)
            for row in events_read:
                if row['id'] == id:
                    id_error = 1
                    if int(row['Remaining Capacity']) >= int(num):
                        if code != 'N':
                            with open('off_ticket.json') as offs:
                                for line in offs.readlines():
                                    roww = json.loads(line)
                                    if roww['id'] == id:
                                        try:
                                            off = int(roww['code_off'][code])
                                            cost = int(row['Price']) * int(num) * (100 - off) / 100
                                            if int(self.money) >= cost:
                                                print(Fore.BLUE + "bought successfully")
                                                ent, remain = event.find_event(id)
                                                ent.remaining_capacity = remain
                                                ent.update_cap(num)
                                                self.update_wallet(cost)
                                                log.info_logger.info(f"Event with ID:{id} with numbers:{num} bought.")
                                                return id_error

                                            else:
                                                print(Fore.RED + "You don't have enough money.")
                                                log.warning_logger.warning(f"{self.user_name} not enough money.")
                                                return id_error
                                        except:
                                            print("code is not correct.")
                                            id_error=1
                                            return id_error
                        else:
                            cost = int(row['Price']) * int(num)
                            if int(self.money) >= cost:
                                print(Fore.BLUE + "Bought successfully")
                                ent, remain = event.find_event(id)
                                ent.remaining_capacity = remain
                                ent.update_cap(num)
                                self.update_wallet(cost)
                                log.info_logger.info(f"Event with ID:{id} with numbers:{num} bought.")
                                return id_error
                            else:
                                print(Fore.RED + "You don't have enough money")
                                log.warning_logger.warning(f"{self.user_name} not enough money.")
                                return id_error
                    else:
                        print(Fore.RED + "Event doesn't have enough capacity")
                        log.warning_logger.warning(f"Event with ID : {id} not enough capacity")
                        return id_error
                else:
                    id_error=0
        return id_error

    def add_file(self, path):
        """
        This function adda created user to file.
        :param path:address of file
        """
        with open(path, "a", newline='') as user_add:
            title = ["user name", "password", "money"]
            csv_file = csv.DictWriter(user_add, fieldnames=title)
            if Path('user.csv').stat().st_size == 0:
                csv_file.writeheader()
            csv_file.writerow({"user name": self.user_name, "password": self.password,
                               "money": self.money})

    def charge_wallet(self, money_1):
        """
        This function add amount of money to attribute money, and enter it to file.
        :param money_1: amount of money that want to add.
        """
        self.money = int(self.money) + int(money_1)
        change = pd.read_csv('user.csv')
        location = 0
        with open('user.csv', 'r+') as users:
            user_read = csv.DictReader(users)
            for row in user_read:
                if row['user name'] == self.user_name:
                    change.loc[location, 'money'] = self.money
                    change.to_csv('user.csv', index=False)
                location += 1

    def update_wallet(self, money):
        """
        After buying update money.
        :param money: amount of money that spend.
        """
        self.money = int(self.money) - int(money)
        change = pd.read_csv('user.csv')
        location = 0
        with open('user.csv', 'r+') as users:
            user_read = csv.DictReader(users)
            for row in user_read:
                if row['user name'] == self.user_name:
                    change.loc[location, 'money'] = self.money
                    change.to_csv('user.csv', index=False)
                location += 1

    def find_money(self):
        """
        this function find money of user name.
        """
        with open('user.csv') as users:
            user_read = csv.DictReader(users)
            for row in user_read:
                if row['user name'] == self.user_name:
                    self.money = row['money']

    def show_information(self):
        """
        This function shows information of user.
        """
        with open('user.csv', 'r') as users:
            user_read = csv.DictReader(users)
            for row in user_read:
                if row['user name'] == self.user_name:
                    password = hash_pas.unhash(row['password'])
                    print(Fore.BLUE + row['user name'], password, row['money'])
