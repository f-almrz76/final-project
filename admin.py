from user import User


class Admin(User):

    def create_event(self):
        print("event  is created")

    def off_ticket(self):
        print("off-ticket is created.")