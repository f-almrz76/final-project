import event
import csv
import json


def get_info():
    print("Enter information of new event.")
    event_info = input("id,name,date,place,total_capacity,price").split(',')
    return event_info


def create_event():
    event_info = get_info()
    new_event = event.Event(*event_info)
    new_event.add_file()


def get_ticket():
    dic = {}
    print("enter code off:")
    print("Name:value,Name:value,...")
    lst = input().split(',')
    for i in lst:
        k, v = i.split(':')
        dic[k] = int(v)
    return dic


def off_ticket(ID):
    with open('Event.csv', 'r') as events:
        event_read = csv.DictReader(events)
        for i in event_read:
            if i['id'] == ID:
                off = get_ticket()
                with open('off_ticket.json', 'a') as offs:
                    json.dump({"id": ID, "code_off": off}, offs)
                    offs.write('\n')
                    break


def show_capacity(name):
    if name == 'all':
        with open('Event.csv', 'r')as events:
            event_read = csv.DictReader(events)
            for row in event_read:
                print(row['Name'] + ':' + row['Remaining Capacity'])
    else:
        with open('Event.csv', 'r') as events:
            event_read = csv.DictReader(events)
            for row in event_read:
                if row['Name'] == name:
                    print(row['Name'] + ':' + row['Remaining Capacity'])
                    break

# student:50,teacher:10,employee:30
# show_capacity('all')
# show_capacity('Thor')
# off_ticket('2')
