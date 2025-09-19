
list_todo = []
completed = []

# 1: viewing tasks
def view():
    if list_todo != []:
        print("\nTO-DO LIST:")
        for index, item in enumerate(list_todo, start=1):
            print(f"{index}. {item}")
    else:
        print("The list is empty.")
    question()

# 2: adding tasks       
def add():
    lets_continue = "y"
    while lets_continue == "y":
        new_item = input("Write a new TO-DO item: ")
        list_todo.append(new_item)
        lets_continue = input("Do you want to add another item? y/n: ")
    question()

# 3: completing or deleting tasks
def comp_del():
    if list_todo != []:
        lets_continue = "y"
        while lets_continue == "y":
            choice = input("Do you want to delete or complete a task? delete/complete: ").lower()
            if choice == "delete" or choice == "complete":
                # Display the list in enumerated format
                print("\nTO-DO LIST:")
                for index, item in enumerate(list_todo, start=1):
                    print(f"{index}. {item}")
                try:
                    index = int(input(f"Which line should be {choice}d? Write a number: "))
                    moved_item = list_todo.pop(index-1)
                    if choice == "complete":
                        completed.append(moved_item)
                        moved_item = ""
                    elif choice == "delete":
                        moved_item = ""
                    else:
                        print("Your answer is wrong, try again.")
                    
                    lets_continue = input("Do you want to complete or delete another task? y/n: ")
                except ValueError:
                    print("Not a number. Try again.")
                except IndexError:
                    print("Number out of range. Try again.")
            else:
                print("Wrong answer. Try again.")
                comp_del()
    else:
        print("The list is empty.")
    question()

# 4: viewing completed tasks       
def view_comp():
    if completed != []:
        print("\nCOMPLETED TASKS:")
        for index, item in enumerate(completed, start=1):
                print(f"{index}. {item}")
    else:
        print("The list is empty.")
    question()

# 5: exit
def exit():
    print("Have a great day!")

    
def question():
    try:
        user_choice = int(input("\nPick a number, do you want to\n1: view the to-do list,\n2: add task,\n3: complete task or delete task\n4: view completed tasks\n5: exit\n"))
        if user_choice == 1:
            view()
        elif user_choice == 2:
            add()
        elif user_choice == 3:
            comp_del()
        elif user_choice == 4:
            view_comp()
        elif user_choice == 5:
            exit()
        else:
            print("Wrong number. Try again.")
            question()
    except ValueError:
        print("Not a number. Try again.")
        question()
        
question()