import data
from cashier import Cashier
from sandwich_maker import SandwichMaker

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(data.resources)
cashier_instance = Cashier()


def main():
    ###  write the rest of the codes ###
    while True:
        choice = input(
            "What would you like? (small/ medium/ large/ off/ report): "
        ).lower()
        if choice == "off":
            print("Turning off the machine.")
            break
        elif choice == "report":
            sandwich_maker_instance.report()
        elif choice in data.recipes:
            sandwich = data.recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                inserted_coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(inserted_coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)

        else:
            print("invalid option. Please choose small, medium, larg, off, or report.")


if __name__ == "__main__":
    main()
