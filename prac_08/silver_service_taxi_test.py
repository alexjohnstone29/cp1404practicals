from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    silver_taxi = SilverServiceTaxi("Hummer", 200, 2)
    print(silver_taxi)
    silver_taxi.start_fare()
    silver_taxi.drive(18)
    print(silver_taxi)
    fare = silver_taxi.added_flagfall()
    print("Total fare is ${:.2f}".format(fare))


main()
