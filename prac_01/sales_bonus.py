"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: "))


def calculate_bonus(sales):
    if sales < 1000:
        bonus = sales * .10
        print(bonus)
    else:
        bonus = sales * .15
        print(bonus)


while sales >= 0:
    calculate_bonus(sales)
    sales = float(input("Enter sales: "))
