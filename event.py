import csv
import pandas as pd
from pathlib import Path
import tabulate


def show_event():
    """
    read events from file and show them.
    """
    table = []
    with open('Event.csv', 'r') as events:
        read_event = csv.reader(events)
        for event in read_event:
            table.append(event)
    print(tabulate.tabulate(table, tablefmt="fancy_grid"))


def find_event(id):
    """
    this function find event from file of events.
    :param id: id of event that want to find
    :return: object of event and remaining capacity.
    """
    with open("Event.csv", 'r') as events:
        event_read = csv.DictReader(events)
        for row in event_read:
            if row['id'] == id:
                evnt = Event(id, row['Name'], row['Date'], row['Place'], row['Total Capacity'], row['Price'])
                remain = row['Remaining Capacity']

    return evnt, remain


def check_id_event(id):
    try:
        with open("Event.csv", 'r') as events:
            event_read = csv.DictReader(events)
            for line in event_read:
                if line['id'] == id:
                    return 0
                else:
                    return 1

    except:
        return 1


class Event:

    def __init__(self, id, name, date, place, total_capacity, price):
        self.id = id
        self.name = name
        self.date = date
        self.place = place
        self.total_capacity = int(total_capacity)
        self.remaining_capacity = int(total_capacity)
        self.price = int(price)

    def update_cap(self, capacity):
        """
        after buy ticket from event update remaining capacity.
        :param capacity: number of ticket that user bought them.
        """
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
        """
        this function append event information to file.
        """
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
