driver_name = input("Driver name:")
start_trip = ""
trip_amount = 0
total_time = 0
total_price = 0

while start_trip != "no":

    taxi_time = 0
    start_trip = input("Would you like to start a new trip:")

    if start_trip == "yes":
        taxi_time = int(input("How long was the taxi ride, (minutes):"))
        trip_amount = trip_amount + 1
        taxi_price = taxi_time * 2 + 10
        total_time = total_time + taxi_time
        total_price = total_price + taxi_price
    elif start_trip == "no":
        print()
    else:
        print("Please enter a valid answer.")

