import register
import admin
import event
import user

while True:
    print("1.Sign in")
    print("2.Sign up")
    print("3.Exit")
    choice = input("Please choose ")
    if choice == "1":
        print("1.Amin")
        print("2.User")
        choice_1 = input("Please choose ")
        if choice_1 == "1":
            code = input("Enter admin code ")
            if code == 'admin123456':
                lst = register.check("admin.csv")
                check = lst[0]
                if check:
                    while True:
                        admin_1 = user.User(lst[1], lst[2])
                        print("what would you like to do : ")
                        print("1.create event.")
                        print("2.create off_ticket")
                        print("3.remaining capacity")
                        print("4.previous")
                        choice_11 = input("please choose")
                        if choice_11 == "1":
                            new_event = admin.create_event()
                            print("new event is created.")
                        elif choice_11 == "2":
                            id_event = input('enter id event:')
                            admin.off_ticket(id_event)
                        elif choice_11 == "3":
                            name_event = input('enter name event or if you want see all event enter all ')
                            admin.show_capacity(name_event)
                        elif choice_11 == "4":
                            break

            else:
                print("your code is wrong!")
        elif choice_1 == "2":
            lst = register.check("user.csv")
            check = lst[0]
            if check:
                while True:
                    user_1 = user.User(lst[1], lst[2])
                    print("what would you like to do : ")
                    print("1.Show list event.")
                    print("2.Buy ticket.")
                    print("3.Charge wallet.")
                    print("4.previous")
                    choice_12 = input("please choose ")
                    if choice_12 == "1":
                        event.show_event()
                    elif choice_12 == "2":
                        money=register.find_money(lst[1])
                        user_1.money=money
                        id_event = input("Which event do you want buy ticket?")
                        num = input("how many tickets do toy want to buy?")
                        code = input("if you have code off please enter it,else print N ")
                        user.User.buy(user_1, id_event, num, code)
                    elif choice_12 == "3":
                        print("How much money do you want to add ")
                        money = input()
                        money_1=register.find_money(lst[1])
                        user_1.money=money_1
                        user.User.charge_wallet(user_1, money)
                    elif choice_12 == "4":
                        break

    elif choice == "2":
        print("1.Amin")
        print("2.User")
        choice_2 = input("Please choose ")
        if choice_2 == "1":
            code = input("Enter admin code ")
            if code == 'admin123456':
                while True:
                    user_name, password = register.enter_user()
                    check = register.check_user(user_name, 'admin.csv')
                    if check == 1:
                        register.register(user_name, password, "admin.csv")
                        print("your account is created.you can sign in.")
                        break
                    elif check == 0:
                        print("user name exists")
            else:
                print("your code is wrong!")
        elif choice_2 == "2":
            while True:
                user_name, password = register.enter_user()
                check = register.check_user(user_name, 'user.csv')
                if check == 1:
                    register.register(user_name, password, "user.csv")
                    print("your account is created.you can sign in. ")
                    break
                elif check == 0:
                    print("user name exists.")

    elif choice == "3":
        break
    else:
        print("Your choice is wrong!")
        continue
