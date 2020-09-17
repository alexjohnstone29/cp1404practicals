
from prac_06.guitar_details import GuitarDetails

guitar_list = []

print("My guitars!")
guitar_name = input("Name: ")
while guitar_name != "":
    guitar_year = int(input("Year: "))
    guitar_cost = int(input("Cost: "))
    print("{} ({}) : {} added.".format(guitar_name, guitar_year, guitar_cost))
    guitar_list.append(GuitarDetails(guitar_name, guitar_year, guitar_cost))
    guitar_name = input("Name: ")

guitar_list.append(GuitarDetails("Gibson L-5 CES", 1922, 16035.40))
guitar_list.append(GuitarDetails("Line 6 JTV-59", 2010, 1512.9))

if guitar_list:
    print("These are my guitars:")
    for i, guitar_list in enumerate(guitar_list, 0):
        vintage = ""
        if guitar_list.is_vintage():
            vintage = "(vintage)"
        print("Guitar {}: {:>15} ({}), worth ${:10,.2f} {}".format(i + 1, guitar_list.name, guitar_list.year, guitar_list.cost, vintage))
