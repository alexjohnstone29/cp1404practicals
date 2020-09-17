

from prac_06.guitar_details import GuitarDetails

gibson = GuitarDetails()
another_guitar = GuitarDetails()

gibson.get_age(1922)
another_guitar.get_age(2013)

print("Gibson L-5 CES get_age() - Expected 98. Got {}".format(gibson.year))
print("Another guitar get_age() - Expected 7. Got {}".format(another_guitar.year))

print("Gibson L-5 CES is_vintage() - Expected True. Got {}".format(gibson.is_vintage()))
print("Another guitar is_vintage() - Expected False. Got {}".format(another_guitar.is_vintage()))
