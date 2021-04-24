import csv


class User:

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.role = "user"

    def buy(self):
        print("you buy ticket")

    def add_file(self,path):
        with open(path, "a", newline='') as user_add:
            csv_file = csv.writer(user_add)
            csv_file.writerow([self.user_name, self.password])