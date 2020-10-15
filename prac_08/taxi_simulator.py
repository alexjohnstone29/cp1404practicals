from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_cost = 0

    print("Let's Drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            taxi_list(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            current_taxi.start_fare()
            drive_distance = int(input("Drive how far? "))
            current_taxi.drive(drive_distance)
            fare = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare))
            total_cost += fare
        else:
            print("Invalid input")
        print("Bill to date: ${:.2f}".format(total_cost))
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(total_cost))


def taxi_list(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
