import csv
import pandas as pd
from pathlib import Path
import json
import event


class User:

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.money = 0

    def buy(self,id,num,code):
        with open('Event.csv','r') as events:
            events_read=csv.DictReader(events)
            for row in events_read:
                if row['id']==id:
                    if int(row['Remaining Capacity']) >= int(num):
                        if code != 'N':
                            with open('off_ticket.json') as offs:
                                for line in offs.readlines():
                                    roww=json.loads(line)
                                    if roww['id']==id:
                                        off=int(roww['code_off'][code])
                                        cost=int(row['Price'])*int(num)*(100-off)/100
                                        with open('user.csv','r') as users:
                                            user_read=csv.DictReader(users)
                                            for u in user_read:
                                                if u['user name']==self.user_name:
                                                    if int(u['money'])>=cost:
                                                        print("bought successfully")
                                                        ent,remain=event.find_event(id)
                                                        ent.remaining_capacity=remain
                                                        ent.update_cap(num)
                                                        self.update_wallet(cost)
                                                    else:
                                                        print('you dont have enough money')
                                                        break

                        else:
                            cost=int(row['Price'])*int(num)
                            with open('user.csv','r') as users:
                                user_read=csv.DictReader(users)
                                for u in user_read:
                                    if u['user name'] == self.user_name:
                                        if int(u['money'])>=cost:
                                            print("bought successfully")
                                            ent,remain=event.find_event(id)
                                            ent.remaining_capacity=remain
                                            ent.update_cap(num)
                                            self.update_wallet(cost)
                                        else:print("dont have enough money")
                    else:print('Event doesnit have enough capacity')



    def add_file(self, path):
        with open(path, "a", newline='') as user_add:
            title = ["user name", "password", "money"]
            csv_file = csv.DictWriter(user_add, fieldnames=title)
            if Path('user.csv').stat().st_size == 0:
                csv_file.writeheader()
            csv_file.writerow({"user name": self.user_name, "password": self.password,
                               "money": self.money})

    def charge_wallet(self, money_1):
        self.money = int(self.money) + int(money_1)
        change = pd.read_csv('user.csv')
        location = 0
        with open('user.csv', 'r+') as users:
            user_read = csv.DictReader(users)
            for row in user_read:
                if row['user name'] == self.user_name:
                    change.loc[location, 'money'] = self.money
                    change.to_csv('user.csv',index=False)
                location += 1

    def update_wallet(self,money):
        self.money=int(self.money)-int(money)
        change=pd.read_csv('user.csv')
        location=0
        with open('user.csv','r+') as users:
            user_read = csv.DictReader(users)
            for row in user_read:
                if row['user name'] == self.user_name:
                    change.loc[location,'money']=self.money
                    change.to_csv('user.csv',index=False)
                location += 1

'''user = User('fateme', 123654)
#user.buy('Thor', 2)
#user.add_file('user.csv')
user.charge_wallet(50000)
user.buy('1', 1,'student')'''
