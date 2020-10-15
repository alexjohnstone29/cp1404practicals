from prac_08.unreliable_car import UnreliableCar


def main():
    car = UnreliableCar("Test car", 100, 20)
    car.drive(50)
    print(car)


main()
