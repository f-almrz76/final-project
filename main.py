from colorama import Fore
import register
import admin
import event
import user
import log

dash = "-" * 100
while True:
    print(Fore.YELLOW + "1.Sign in")
    print(Fore.YELLOW + "2.Sign up")
    print(Fore.YELLOW + "3.Exit")
    choice = input()
    print(Fore.GREEN + dash)
    if choice == "1":
        print(Fore.YELLOW + "1.Admin")
        print(Fore.YELLOW + "2.User")
        choice_1 = input()
        print(Fore.GREEN + dash)
        if choice_1 == "1":
            code = input(Fore.LIGHTBLUE_EX + "Enter admin code ")
            if code == 'admin123456':
                lst = register.check("admin.csv")
                check = lst[0]
                print(Fore.GREEN + dash)
                if check:
                    while True:
                        admin_1 = admin.Admin(lst[1], lst[2])
                        print(Fore.YELLOW + "1.create event.")
                        print(Fore.YELLOW + "2.create off_ticket")
                        print(Fore.YELLOW + "3.remaining capacity")
                        print(Fore.YELLOW + "4.previous")
                        choice_11 = input()
                        print(Fore.GREEN + dash)
                        if choice_11 == "1":
                            while True:
                                event_info = admin.get_info()
                                check1 = event.check_id_event(event_info[0])
                                if check1 or check1 == None:
                                    check_1 = admin.create_event(event_info)
                                    if check_1:
                                        log.info_logger.info(f"{event_info} is created.")
                                        print(Fore.BLUE + "new event is created.")
                                        break
                                    else:
                                        print(Fore.RED + "number of information isn't correct.")
                                else:
                                    print(Fore.RED + f" event with ID :{event_info[0]} exists.")
                            print(Fore.GREEN + dash)
                        elif choice_11 == "2":
                            id_event = input(Fore.LIGHTBLUE_EX + 'Enter id of event:')
                            check_2 = admin.off_ticket(id_event)
                            if check_2:
                                print(Fore.BLUE + f"discounts of tickets for event with ID : {id_event} is created.")
                            else:
                                print(Fore.RED + f"ID:{id_event} is wrong, because this event doesn't exist.")
                            print(Fore.GREEN + dash)
                        elif choice_11 == "3":
                            id_event = input(Fore.LIGHTBLUE_EX + 'id event or if you want see all event enter all ')
                            try:
                                admin.show_capacity(id_event)
                                print(Fore.GREEN + dash)
                            except:
                                print("Please try again.")
                                log.warning_logger.error(FileNotFoundError,exc_info=True)
                                print(Fore.GREEN + dash)
                        elif choice_11 == "4":
                            print(Fore.GREEN + dash)
                            break

            else:
                print(Fore.RED + "your code is wrong!")
                print(Fore.GREEN + dash)
        elif choice_1 == "2":
            lst = register.check("user.csv")
            check = lst[0]
            if check:
                while True:
                    user_1 = user.User(lst[1], lst[2])
                    print(Fore.YELLOW + "1.Show list event.")
                    print(Fore.YELLOW + "2.Buy ticket.")
                    print(Fore.YELLOW + "3.Charge wallet.")
                    print(Fore.YELLOW + "4.Show information user.")
                    print(Fore.YELLOW + "5.previous")
                    choice_12 = input()
                    if choice_12 == "1":
                        event.show_event()
                        print(Fore.GREEN + dash)
                    elif choice_12 == "2":
                        user_1.find_money()
                        id_event = input(Fore.LIGHTBLUE_EX + "Which event do you want buy ticket?")
                        num = input(Fore.LIGHTBLUE_EX + "how many tickets do toy want to buy?")
                        code = input(Fore.LIGHTBLUE_EX + "if you have code off please enter it,else print N ")
                        id_error = user.User.buy(user_1, id_event, num, code)
                        if id_error == 0:
                            print(f"Event with ID : {id_event} doesn't exist.")
                            log.warning_logger.error(f"Event with ID : {id_event} doesn't exist.")
                        print(Fore.GREEN + dash)
                    elif choice_12 == "3":
                        print(Fore.LIGHTBLUE_EX + "How much money do you want to add ")
                        money = input()
                        try:
                            user_1.find_money()
                            user.User.charge_wallet(user_1, money)
                            print(f"Your wallet charges {money}")
                        except:
                            print("Not charge! please try again.")
                            log.warning_logger.error(FileNotFoundError, exc_info=True)
                        print(Fore.GREEN + dash)
                    elif choice_12 == "4":
                        user_1.show_information()
                        print(Fore.GREEN + dash)
                    elif choice_12 == "5":
                        print(Fore.GREEN + dash)
                        break

    elif choice == "2":
        print(Fore.YELLOW + "1.Admin")
        print(Fore.YELLOW + "2.User")
        choice_2 = input()
        if choice_2 == "1":
            code = input(Fore.LIGHTBLUE_EX + "Enter admin code ")
            if code == 'admin123456':
                while True:
                    user_name, password = register.enter_user()
                    check = register.check_user(user_name, 'admin.csv')

                    if check == 1 or check == None:
                        register.register_admin(user_name, password, "admin.csv")
                        log.info_logger.info(f"admin with admin_name : {user_name} registers.")
                        print(Fore.BLUE + "your account is created.you can sign in.")
                        print(Fore.GREEN + dash)
                        break
                    elif check == 0:
                        print(Fore.RED + "user name exists")
                        print(Fore.GREEN + dash)
                        continue
            else:
                print(Fore.RED + "your code is wrong!")
                print(Fore.GREEN + dash)
        elif choice_2 == "2":
            while True:
                user_name, password = register.enter_user()
                check = register.check_user(user_name, 'user.csv')
                if check == 1 or check == None:
                    register.register_user(user_name, password, "user.csv")
                    log.info_logger.info(f"user with user_name : {user_name} registers.")
                    print(Fore.BLUE + "your account is created.you can sign in. ")
                    print(Fore.GREEN + dash)
                    break
                elif check == 0:
                    print(Fore.RED + "user name exists.")
                    print(Fore.GREEN + dash)
                    continue

    elif choice == "3":
        break
    else:
        print("Your choice is wrong!")
        continue
