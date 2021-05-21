import event
import csv
import json
from colorama import Fore
from pathlib import Path


def get_info():
    """
    this function gets information of event from admin.
    :return: list of information
    """
    print(Fore.LIGHTBLUE_EX + "Enter information of new event.")
    print(Fore.LIGHTBLUE_EX + "id,name,date,place,total_capacity,price")
    event_info = input().split(',')
    return event_info


def create_event(event_info):
    """
    this function creates object of event and add to event file.
    """
    try:
        new_event = event.Event(*event_info)
        new_event.add_file()

        return 1
    except:
        return 0


def get_ticket():
    """
    this function get information discount for event.
    :return: a dictionary of discounts.
    """
    dic = {}
    print("enter code off:")
    print("Name:value,Name:value,...")
    lst = input().split(',')
    for i in lst:
        k, v = i.split(':')
        dic[k] = int(v)
    return dic


def off_ticket(ID):
    """
    this function defines discounts and add to file ticket.
    :param ID: id of event that want to create discounts.
    """
    with open('Event.csv', 'r') as events:
        event_read = csv.DictReader(events)
        for i in event_read:
            if i['id'] == ID:
                off = get_ticket()
                with open('off_ticket.json', 'a') as offs:
                    json.dump({"id": ID, "code_off": off}, offs)
                    offs.write('\n')
                    check = 1
                    break
        else:
            check = 0
    return check


def show_capacity(ID):
    """
    show capacity of events.
    :param ID: ID of event that want to show capacity and if ID = all show all
    of capacity of events.
    """
    if ID == 'all':
        with open('Event.csv', 'r')as events:
            event_read = csv.DictReader(events)
            for row in event_read:
                print(Fore.BLUE + row['id'] + ')' + row['Name'] + ':' + row['Remaining Capacity'])
    else:
        with open('Event.csv', 'r') as events:
            event_read = csv.DictReader(events)
            for row in event_read:
                if row['id'] == ID:
                    print(Fore.BLUE + row['id'] + ')' + row['Name'] + ':' + row['Remaining Capacity'])
                    break


class Admin:
    def __init__(self, admin_name, password):
        self.user_name = admin_name
        self.password = password

    def add_file(self, path):
        """
        This function adda created user to file.
        :param path:address of file
        """
        with open(path, "a", newline='') as user_add:
            title = ["user name", "password"]
            csv_file = csv.DictWriter(user_add, fieldnames=title)
            if Path('admin.csv').stat().st_size == 0:
                csv_file.writeheader()
            csv_file.writerow({"user name": self.user_name, "password": self.password})