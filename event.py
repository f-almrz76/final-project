import csv


def get_info():
    """This function get information from admin"""
    pass


def show_event():
    print("list event")


class Event:

    def __init__(self, name, date, place, total_capacity, remaining_capacity, price):
        self.name = name
        self.date = date
        self.place = place
        self.total_capacity = total_capacity
        self.remaining_capacity = remaining_capacity
        self.price = price

    def update(self, capacity):
        self.remaining_capacity = self.total_capacity - capacity

    def add_file(self):
        with open("Event.csv", "a", newline='') as event_add:
            title = ["Name", "Date", "Place", "Total Capacity", "Remaining Capacity", "Price"]
            csv_file = csv.DictWriter(event_add, fieldnames=title)
            csv_file.writeheader()
            csv_file.writerow({
                'Name': self.name,
                'Date': self.date,
                'Place': self.place,
                'Total Capacity': self.total_capacity,
                'Remaining Capacity': self.remaining_capacity,
                'Price': self.price
            })



