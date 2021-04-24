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
                check,user_name,password=register.check("admin.csv")

                if check :
                    while True:
                        admin_1=user.User(user_name,password)
                        print("what would you like to do : ")
                        print("1.create event.")
                        print("2.create off_ticket")
                        print("3.previous")
                        choice_11=input("please choose")
                        if choice_11 == "1":
                            admin.Admin.create_event(admin_1)
                        elif choice_11 == "2":
                            admin.Admin.off_ticket(admin_1)
                        elif choice_11 == "3":
                            break

            else:
                print("your code is wrong!")
        elif choice_1 == "2":
            check,user_name,password=register.check("user.csv")
            if check:
                while True:
                    user_1=user.User(user_name,password)
                    print("what would you like to do : ")
                    print("1.Show list event.")
                    print("2.Buy ticket.")
                    print("3.previous")
                    choice_12=input("please choose ")
                    if choice_12 == "1":
                        event.show_event()
                    elif choice_12 == "2":
                        user.User.buy(user_1)
                    elif choice_12 == "3":
                        break

    elif choice == "2":
        print("1.Amin")
        print("2.User")
        choice_2 = input("Please choose ")
        if choice_2 == "1":
            code = input("Enter admin code ")
            if code == 'admin123456':
                register.register("admin.csv")
            else:
                print("your code is wrong!")
        elif choice_1 == "2":
            register.register("user.csv")
    elif choice == "3":
        break
    else:
        print("Your choice is wrong!")
        continue

