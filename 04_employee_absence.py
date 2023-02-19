def employee_input():

    employee_list = []

    while True:
        employee_name = input("Employee name:")
        if employee_name != "$":
            absence_days = int(input("How many days have you been absent in the "
                                     "past year:"))
            print()
        else:
            break

        employee_list.append([employee_name, absence_days])

    employee_output(employee_list)


def employee_output(_employee_list):
    total_absence = 0
    employee_amount = 0
    above_average = []
    no_absence = []
    most_absent_days = 0
    most_absent_name = ""

    for employees in _employee_list:
        total_absence += employees[1]
        employee_amount += 1

        if employees[1] >= most_absent_days:
            most_absent_days = employees[1]
            most_absent_name = employees[0]

    average_absence = total_absence / employee_amount

    for employees in _employee_list:
        if employees[1] >= average_absence:
            above_average.append(employees)
        elif employees[1] == 0:
            no_absence.append(employees)

    print(f"Average number of days staff were absent: {average_absence:.2f}")

    print(f"The person who was absent the most was: {most_absent_name}, "
          f"with an absence of {most_absent_days} days.")
    print()

    print("People who haven't been absent are:")
    for employees in no_absence:
        print(employees[0])
    print()

    print("List of people absent above average:")
    for employees in above_average:
        print(employees)


# Main Routine
employee_input()
