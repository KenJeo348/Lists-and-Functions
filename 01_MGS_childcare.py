def main():
    choice = 0
    child_list = []
    while choice != 5:
        print("\n"
              "<================================================>\n"
              "Welcome to MGS Childcare\n"
              "What would you like to do? "
              "Please choose one of the items below\n"
              "<================================================>\n"
              "\n"
              "1:Drop off a child.\n"
              "2:Pick up a child.\n"
              "3:Calculate cost.\n"
              "4:Print roll.\n"
              "5:Exit the system\n"
              "\n")
        choice = int(input("Enter your choice (From 1-5):"))
        print()

        if choice == 1:
            drop_off(child_list)
        elif choice == 2:
            pick_up(child_list)
            print(child_list)
        elif choice == 3:
            calc_cost()
        elif choice == 4:
            print_roll(child_list)
        else:
            print("Goodbye")


def drop_off(_child_list):
    child_name = input("What is the name of your child:")
    _child_list.append(child_name)


def pick_up(_child_list):
    while True:
        try:
            _child_name = input("What is the name of your child:")
            _child_list.remove(_child_name)
            break
        except ValueError:
            print("Please enter a valid name.")


def calc_cost():
    HOURLY_PRICE = 12
    hours = int(input("How long would you like to leave the child with us:"))
    cost = HOURLY_PRICE * hours
    print(f"To leave your child for {hours} hours, "
          f"you would have to pay ${cost} dollars.")


def print_roll(_child_list):
    print("The children staying at our childcare are:")
    for children in _child_list:
        print(children)


# Main Routine
main()
