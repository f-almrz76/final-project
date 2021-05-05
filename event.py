import csv
import pandas as pd
from pathlib import Path


def show_event():
    with open('Event.csv', 'r') as events:
        read_event = csv.reader(events)
        for event in read_event:
            print(event)


class Event:

    def __init__(self, id, name, date, place, total_capacity, price):
        self.id = id
        self.name = name
        self.date = date
        self.place = place
        self.total_capacity = int(total_capacity)
        self.remaining_capacity = int(total_capacity)
        self.price = int(price)

    def update_cap(self,capacity):
        self.remaining_capacity = int(self.remaining_capacity) - int(capacity)
        change = pd.read_csv('Event.csv')
        location = 0
        with open('Event.csv', 'r+') as events:
            events_read = csv.DictReader(events)
            for row in events_read:
                if row['id'] == self.id:
                    change.loc[location, 'Remaining Capacity'] = self.remaining_capacity
                    change.to_csv('Event.csv', index=False)
                location += 1

    def add_file(self):
        with open("Event.csv", "a", newline='') as event_add:
            title = ["id", "Name", "Date", "Place", "Total Capacity", "Remaining Capacity",
                     "Price"]
            csv_file = csv.DictWriter(event_add, fieldnames=title)
            if Path("Event.csv").stat().st_size == 0:
                csv_file.writeheader()
            csv_file.writerow({
                'id': self.id,
                'Name': self.name,
                'Date': self.date,
                'Place': self.place,
                'Total Capacity': self.total_capacity,
                'Remaining Capacity': self.remaining_capacity,
                'Price': self.price,

            })


def find_event(id):
    with open("Event.csv", 'r') as events:
        event_read = csv.DictReader(events)
        for row in event_read:
            if row['id'] == id:
                evnt = Event(id, row['Name'], row['Date'], row['Place'], row['Total Capacity'], row['Price'])
                remain = row['Remaining Capacity']

    return evnt, remain


'''
mem = Event(*[3,'Thor', '9 / 8', 'cinema', 60, 10000])
mem.add_file()
mem.update_cap(20)
#show_event()
'''
