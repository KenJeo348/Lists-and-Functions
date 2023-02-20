driver_name = input("Enter driver's name:")

total_time = 0
total_income = 0
BASE_COST = 10
PER_MINUTE_COST = 2
start_trip = "y"
trip_amount = 0

while start_trip != "n":
    trip_time = int(input("How long did the trip take, (in minutes):"))
    trip_amount = trip_amount + 1
    total_time = total_time + trip_time
    trip_cost = BASE_COST + trip_time * PER_MINUTE_COST
    total_income = total_income + trip_cost
    print(f"The cost of this trip was ${trip_cost}")

    start_trip = input("Would you like to start a new trip, (y or n):")

average_time = total_time / trip_amount
average_cost = total_income / trip_amount

print(f"Taxi driver: {driver_name}\n"
      f"Total time for all trips: {total_time} minutes.\n"
      f"Average time of all trips: {average_time:.2f} minutes.\n"
      f"Total income for the day: ${total_income:.2f} dollars. \n"
      f"Average cost of all trips: ${average_cost:.2f}")


