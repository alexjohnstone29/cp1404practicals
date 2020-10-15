from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    silver_taxi = SilverServiceTaxi("Hummer", 200, 2)
    print(silver_taxi)
    silver_taxi.start_fare()
    silver_taxi.drive(18)
    print(silver_taxi)
    print("Fare cost is ${:.2f}".format(silver_taxi.get_fare()))


main()
